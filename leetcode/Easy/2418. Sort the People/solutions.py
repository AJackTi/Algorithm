def sortPeople(names: List[str], heights: List[int]) -> List[str]:
        return [height for _, height in sorted([(height, name) for name, height in zip(names, heights)], reverse=True)]