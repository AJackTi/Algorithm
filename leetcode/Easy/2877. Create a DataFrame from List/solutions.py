import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    student_id = []
    age = []
    for element in student_data:
        student_id.append(element[0])
        age.append(element[1])
    
    return pd.DataFrame({"student_id": student_id,
                        "age": age})