from typing import Tuple, List, Dict

_RESOURCE_PATH: str = "/{resource:path}"


def match_path(path_patterns: List[str], actual_path: str) -> Tuple[bool, str, Dict]:
    for path_pattern in path_patterns:
        if path_pattern == _RESOURCE_PATH:
            return True, path_pattern, [(path_pattern.strip("/"), actual_path)]
        path_pattern_elements = path_pattern.strip("/").split("/")
        actual_path_elements = actual_path.strip("/").split("/")
        if len(path_pattern_elements) != len(actual_path_elements):
            continue
        different_paths = {a[0]: a[1] for a in zip(path_pattern_elements, actual_path_elements) if a[0] != a[1]}
        path_parameters = {key.strip("{}"): val for key, val in different_paths.items() if
                           key.startswith("{") and key.endswith("}")}
        if len(path_parameters) == len(different_paths):
            return True, path_pattern, path_parameters

    return False, "", {}
