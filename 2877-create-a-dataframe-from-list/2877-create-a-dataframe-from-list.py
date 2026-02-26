import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df=pd.DataFrame(data=student_data,columns=["student_id","age"])
    return df