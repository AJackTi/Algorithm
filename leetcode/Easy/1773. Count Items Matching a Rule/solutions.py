def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key={"type":0, "color":1, "name":2}
        return sum(v[key[ruleKey]]==ruleValue for v in items) 