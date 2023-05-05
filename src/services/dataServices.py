import pandas as pd

class ExcelFileService:
  def __init__(self, filename):
    self.filename = filename
  
  def read_file(self):
    df = pd.read_excel(self.filename)
    
    # convert dataframe to list of dictionaries
    data = df.to_dict(orient='records')
    
    return data
  
  

data_service = ExcelFileService('example.xlsx')

print(data_service.read_file())
