import pandas as pd
import time
import json
# from .models import Company



URL = "https://www.zse.co.zw/price-sheet/"
     

try:

    dataframe = pd.read_html(URL, skiprows=1)
    df = dataframe[0][3:]
    dataframe.columns = [
            "Name",
            "None",
            "None",
            "Opening_Price",
            "Closing_Price",
            "Volume_Traded",
        ]

    # Lets filter the columns we are concerned with
    df_trades = dataframe[
            ["Name", "Opening_Price", "Closing_Price", "Volume_Traded"]
        ]
        # Drop all the columns with no data or missing all data
    df = df_trades.dropna(how="all").set_index("Name")
    print(df)

    json_list = json.loads(json.dumps(df.T.to_dict().values()))
    import pdb;pdb.set_trace()

    for dic in json_list:
        Company.objects.update_or_create(**dic)


except Exception as e:
    print(f'error occured:  {e}')

