import pandas as pd
from tabulate import tabulate


class ExcelFileService:
  def __init__(self, filename):
    self.filename = filename
  
  def read_file(self):
    df = pd.read_excel(self.filename)
    data = df.to_dict(orient='records')
    return data
  
  def update_file(self, data):
    df = pd.DataFrame(data)
    
    with pd.ExcelWriter(self.filename) as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)
  
  def format_data(self, data):
    df = pd.DataFrame(data)
    print(tabulate(df, headers='keys', tablefmt='psql'))
