import json
from pathlib import Path
from spec_loader import FunctionInfo

# management callback function ID
class CallbackIdManager:
    # constructor
    def __init__(self, cache_path: Path):
        self.cache_path = cache_path
    
    # set callback function ID using cache
    def set_function_id(self, function_list: list[FunctionInfo]):
        # load current cache file
        cache = self._load_cache()
        # remove unused function from cache
        is_updated = self._clean_cache(function_list, cache)
        used_ids = set(int(id, 16) for id in cache.values())
        current_ids = set[int]()

        # set ID to each function
        for func in function_list:
            key = self._make_key(func)
            if key in cache and not int(cache[key], 16) in current_ids:
                # this function is in cache, so set same ID
                func.id = int(cache[key], 16)
                current_ids.add(func.id)
            else:
                # this function is not in cache or ID is duplicated, so set new ID
                new_id = self._find_unused_id(used_ids)
                func.id = new_id
                current_ids.add(func.id)
                cache[key] = f'0x{new_id:04X}'
                used_ids.add(new_id)
                is_updated = True
        
        if is_updated:
            # cache is updated, so save to file
            self._save_cache(cache)
    
    # load cache file, this is JSON format
    def _load_cache(self) -> dict:
        if not self.cache_path.exists():
            return {}
        with self.cache_path.open("r", encoding="utf-8") as f:
            return json.load(f)
        
    # remove unused function from cache
    def _clean_cache(self, function_list: list[FunctionInfo], cache: dict) -> bool:
        is_updated = False
        current_keys = {self._make_key(func) for func in function_list}
        cached_keys = set(cache.keys())
        unused_keys = cached_keys - current_keys
        for key in unused_keys:
            is_updated = True
            del cache[key]
        return is_updated
        
    # save cahce to JSON file
    def _save_cache(self, cache: dict):
        with self.cache_path.open("w", encoding="utf-8") as f:
            json.dump(cache, f, indent=2, sort_keys=True)
        
    # make key for JSON, ex. "func(bool,int,string)"
    def _make_key(self, func: FunctionInfo):
        arg_type_list = [arg.type for arg in func.args]
        return f'{func.name}({",".join(arg_type_list)})'
        
    # find unused callback function ID
    def _find_unused_id(self, used_ids: set[int]) -> int:
        id = 1
        while id in used_ids:
            id += 1
        return id
