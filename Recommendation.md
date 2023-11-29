```python
!pip install scipy
```

    Collecting scipy
      Downloading scipy-1.11.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
    [2K     [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m60.4/60.4 kB[0m [31m375.2 kB/s[0m eta [36m0:00:00[0m kB/s[0m eta [36m0:00:01[0m:01[0m
    [?25hRequirement already satisfied: numpy<1.28.0,>=1.21.6 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from scipy) (1.25.0)
    Downloading scipy-1.11.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (36.6 MB)
    [2K   [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m36.6/36.6 MB[0m [31m96.5 kB/s[0m eta [36m0:00:00[0mm eta [36m0:00:01[0m[36m0:00:14[0mm
    [?25hInstalling collected packages: scipy
    Successfully installed scipy-1.11.4



```python
!pip install pandas numpy 
```

    Requirement already satisfied: pandas in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (2.0.2)
    Requirement already satisfied: numpy in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (1.25.0)
    Requirement already satisfied: python-dateutil>=2.8.2 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pandas) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pandas) (2023.3)
    Requirement already satisfied: tzdata>=2022.1 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pandas) (2023.3)
    Requirement already satisfied: six>=1.5 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)



```python
!pip install scikit-posthocs
```

    Collecting scikit-posthocs
      Using cached scikit_posthocs-0.8.0-py3-none-any.whl.metadata (5.9 kB)
    Requirement already satisfied: numpy in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from scikit-posthocs) (1.25.0)
    Requirement already satisfied: scipy in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from scikit-posthocs) (1.11.4)
    Collecting statsmodels (from scikit-posthocs)
      Downloading statsmodels-0.14.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (10.1 MB)
    [2K     [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m10.1/10.1 MB[0m [31m332.5 kB/s[0m eta [36m0:00:00[0mm eta [36m0:00:01[0m[36m0:00:01[0m
    [?25hRequirement already satisfied: pandas>=0.20.0 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from scikit-posthocs) (2.0.2)
    Collecting seaborn (from scikit-posthocs)
      Downloading seaborn-0.13.0-py3-none-any.whl.metadata (5.3 kB)
    Collecting matplotlib (from scikit-posthocs)
      Downloading matplotlib-3.8.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
    Requirement already satisfied: python-dateutil>=2.8.2 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pandas>=0.20.0->scikit-posthocs) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pandas>=0.20.0->scikit-posthocs) (2023.3)
    Requirement already satisfied: tzdata>=2022.1 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from pandas>=0.20.0->scikit-posthocs) (2023.3)
    Collecting contourpy>=1.0.1 (from matplotlib->scikit-posthocs)
      Downloading contourpy-1.2.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
    Collecting cycler>=0.10 (from matplotlib->scikit-posthocs)
      Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
    Collecting fonttools>=4.22.0 (from matplotlib->scikit-posthocs)
      Downloading fonttools-4.45.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (155 kB)
    [2K     [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m155.2/155.2 kB[0m [31m772.2 kB/s[0m eta [36m0:00:00[0m kB/s[0m eta [36m0:00:01[0m:01[0m
    [?25hCollecting kiwisolver>=1.3.1 (from matplotlib->scikit-posthocs)
      Downloading kiwisolver-1.4.5-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl.metadata (6.4 kB)
    Requirement already satisfied: packaging>=20.0 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from matplotlib->scikit-posthocs) (23.1)
    Requirement already satisfied: pillow>=8 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from matplotlib->scikit-posthocs) (10.0.0)
    Collecting pyparsing>=2.3.1 (from matplotlib->scikit-posthocs)
      Using cached pyparsing-3.1.1-py3-none-any.whl.metadata (5.1 kB)
    Collecting importlib-resources>=3.2.0 (from matplotlib->scikit-posthocs)
      Downloading importlib_resources-6.1.1-py3-none-any.whl.metadata (4.1 kB)
    Collecting patsy>=0.5.2 (from statsmodels->scikit-posthocs)
      Using cached patsy-0.5.3-py2.py3-none-any.whl (233 kB)
    Requirement already satisfied: zipp>=3.1.0 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from importlib-resources>=3.2.0->matplotlib->scikit-posthocs) (3.15.0)
    Requirement already satisfied: six in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from patsy>=0.5.2->statsmodels->scikit-posthocs) (1.16.0)
    Using cached scikit_posthocs-0.8.0-py3-none-any.whl (32 kB)
    Downloading matplotlib-3.8.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
    [2K   [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m11.6/11.6 MB[0m [31m995.6 kB/s[0m eta [36m0:00:00[0meta [36m0:00:01[0m[36m0:00:01[0mm0m
    [?25hDownloading seaborn-0.13.0-py3-none-any.whl (294 kB)
    [2K   [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m294.6/294.6 kB[0m [31m1.0 MB/s[0m eta [36m0:00:00[0m[31m1.0 MB/s[0m eta [36m0:00:01[0mm
    [?25hDownloading contourpy-1.2.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (310 kB)
    [2K   [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m311.0/311.0 kB[0m [31m869.7 kB/s[0m eta [36m0:00:00[0mm eta [36m0:00:01[0m36m0:00:01[0m
    [?25hDownloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
    Downloading fonttools-4.45.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
    [2K   [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m4.6/4.6 MB[0m [31m888.2 kB/s[0m eta [36m0:00:00[0mm eta [36m0:00:01[0m[36m0:00:01[0m
    [?25hDownloading importlib_resources-6.1.1-py3-none-any.whl (33 kB)
    Downloading kiwisolver-1.4.5-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
    [2K   [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.6/1.6 MB[0m [31m1.0 MB/s[0m eta [36m0:00:00[0mm eta [36m0:00:01[0m[36m0:00:01[0m0m
    [?25hUsing cached pyparsing-3.1.1-py3-none-any.whl (103 kB)
    Installing collected packages: pyparsing, patsy, kiwisolver, importlib-resources, fonttools, cycler, contourpy, matplotlib, statsmodels, seaborn, scikit-posthocs
    Successfully installed contourpy-1.2.0 cycler-0.12.1 fonttools-4.45.1 importlib-resources-6.1.1 kiwisolver-1.4.5 matplotlib-3.8.2 patsy-0.5.3 pyparsing-3.1.1 scikit-posthocs-0.8.0 seaborn-0.13.0 statsmodels-0.14.0



```python
!pip install sklearn
```

    Collecting sklearn
      Downloading sklearn-0.0.post11.tar.gz (3.6 kB)
      Preparing metadata (setup.py) ... [?25ldone
    [?25hBuilding wheels for collected packages: sklearn
      Building wheel for sklearn (setup.py) ... [?25ldone
    [?25h  Created wheel for sklearn: filename=sklearn-0.0.post11-py3-none-any.whl size=2369 sha256=16869e2690058394401659f793c36aa68149c8f6b3051dd249457d38e6367f04
      Stored in directory: /home/ki3ani/.cache/pip/wheels/9e/9e/4c/184e84f4ce918378a9ec9adafd1b6b73bea45f0a4a7855b6ce
    Successfully built sklearn
    Installing collected packages: sklearn
    Successfully installed sklearn-0.0.post11



```python
!pip install scikit-learn
```

    Collecting scikit-learn
      Downloading scikit_learn-1.3.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
    Requirement already satisfied: numpy<2.0,>=1.17.3 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from scikit-learn) (1.25.0)
    Requirement already satisfied: scipy>=1.5.0 in /home/ki3ani/.pyenv/versions/3.9.0/lib/python3.9/site-packages (from scikit-learn) (1.11.4)
    Collecting joblib>=1.1.1 (from scikit-learn)
      Using cached joblib-1.3.2-py3-none-any.whl.metadata (5.4 kB)
    Collecting threadpoolctl>=2.0.0 (from scikit-learn)
      Using cached threadpoolctl-3.2.0-py3-none-any.whl.metadata (10.0 kB)
    Downloading scikit_learn-1.3.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (10.9 MB)
    [2K   [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m10.9/10.9 MB[0m [31m93.3 kB/s[0m eta [36m0:00:00[0mm eta [36m0:00:01[0m[36m0:00:04[0m
    [?25hUsing cached joblib-1.3.2-py3-none-any.whl (302 kB)
    Using cached threadpoolctl-3.2.0-py3-none-any.whl (15 kB)
    Installing collected packages: threadpoolctl, joblib, scikit-learn
    Successfully installed joblib-1.3.2 scikit-learn-1.3.2 threadpoolctl-3.2.0



```python
import pandas as pd
from scipy.stats import zscore
import numpy as np
import scipy.stats as stats
from scipy.stats import kruskal
import scikit_posthocs as sp
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
```


```python
# Define the file paths for the datasets
file_paths = {
    'order_items': 'data/olist_order_items_dataset.csv',
    'products': 'data/olist_products_dataset.csv',
    'customers': 'data/olist_customers_dataset.csv',
    'order-reviews': 'data/olist_order_reviews_dataset.csv',
    'orders': 'data/olist_orders_dataset.csv',
    'order-payments': 'data/olist_order_payments_dataset.csv',

}

# Function to load datasets
def load_datasets(file_paths):
    data = {}
    for name, path in file_paths.items():
        data[name] = pd.read_csv(path)
    return data

# Load the datasets
loaded_data = load_datasets(file_paths)

# Accessing individual DataFrames
order_items_df = loaded_data['order_items']
products_df = loaded_data['products']
customers_df = loaded_data['customers']
order_reviews_df = loaded_data['order-reviews']
orders_df = loaded_data['orders']
order_payments_df = loaded_data['order-payments']

# Display basic info about the loaded datasets
for name, df in loaded_data.items():
    print(f"--- {name} ---")
    print(df.head())
    print(df.info())
    print("---------------")

```

    --- order_items ---
                               order_id  order_item_id  \
    0  00010242fe8c5a6d1ba2dd792cb16214              1   
    1  00018f77f2f0320c557190d7a144bdd3              1   
    2  000229ec398224ef6ca0657da4fc703e              1   
    3  00024acbcdf0a6daa1e931b038114c75              1   
    4  00042b26cf59d7ce69dfabb4e55b4fd9              1   
    
                             product_id                         seller_id  \
    0  4244733e06e7ecb4970a6e2683c13e61  48436dade18ac8b2bce089ec2a041202   
    1  e5f2d52b802189ee658865ca93d83a8f  dd7ddc04e1b6c2c614352b383efe2d36   
    2  c777355d18b72b67abbeef9df44fd0fd  5b51032eddd242adc84c38acab88f23d   
    3  7634da152a4610f1595efa32f14722fc  9d7a1d34a5052409006425275ba1c2b4   
    4  ac6c3623068f30de03045865e4e10089  df560393f3a51e74553ab94004ba5c87   
    
       shipping_limit_date   price  freight_value  
    0  2017-09-19 09:45:35   58.90          13.29  
    1  2017-05-03 11:05:13  239.90          19.93  
    2  2018-01-18 14:48:30  199.00          17.87  
    3  2018-08-15 10:10:18   12.99          12.79  
    4  2017-02-13 13:57:51  199.90          18.14  
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 112650 entries, 0 to 112649
    Data columns (total 7 columns):
     #   Column               Non-Null Count   Dtype  
    ---  ------               --------------   -----  
     0   order_id             112650 non-null  object 
     1   order_item_id        112650 non-null  int64  
     2   product_id           112650 non-null  object 
     3   seller_id            112650 non-null  object 
     4   shipping_limit_date  112650 non-null  object 
     5   price                112650 non-null  float64
     6   freight_value        112650 non-null  float64
    dtypes: float64(2), int64(1), object(4)
    memory usage: 6.0+ MB
    None
    ---------------
    --- products ---
                             product_id  product_category_name  \
    0  1e9e8ef04dbcff4541ed26657ea517e5             perfumaria   
    1  3aa071139cb16b67ca9e5dea641aaa2f                  artes   
    2  96bd76ec8810374ed1b65e291975717f          esporte_lazer   
    3  cef67bcfe19066a932b7673e239eb23d                  bebes   
    4  9dc1a7de274444849c219cff195d0b71  utilidades_domesticas   
    
       product_name_lenght  product_description_lenght  product_photos_qty  \
    0                 40.0                       287.0                 1.0   
    1                 44.0                       276.0                 1.0   
    2                 46.0                       250.0                 1.0   
    3                 27.0                       261.0                 1.0   
    4                 37.0                       402.0                 4.0   
    
       product_weight_g  product_length_cm  product_height_cm  product_width_cm  
    0             225.0               16.0               10.0              14.0  
    1            1000.0               30.0               18.0              20.0  
    2             154.0               18.0                9.0              15.0  
    3             371.0               26.0                4.0              26.0  
    4             625.0               20.0               17.0              13.0  
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 32951 entries, 0 to 32950
    Data columns (total 9 columns):
     #   Column                      Non-Null Count  Dtype  
    ---  ------                      --------------  -----  
     0   product_id                  32951 non-null  object 
     1   product_category_name       32341 non-null  object 
     2   product_name_lenght         32341 non-null  float64
     3   product_description_lenght  32341 non-null  float64
     4   product_photos_qty          32341 non-null  float64
     5   product_weight_g            32949 non-null  float64
     6   product_length_cm           32949 non-null  float64
     7   product_height_cm           32949 non-null  float64
     8   product_width_cm            32949 non-null  float64
    dtypes: float64(7), object(2)
    memory usage: 2.3+ MB
    None
    ---------------
    --- customers ---
                            customer_id                customer_unique_id  \
    0  06b8999e2fba1a1fbc88172c00ba8bc7  861eff4711a542e4b93843c6dd7febb0   
    1  18955e83d337fd6b2def6b18a428ac77  290c77bc529b7ac935b93aa66c333dc3   
    2  4e7b3e00288586ebd08712fdd0374a03  060e732b5b29e8181a18229c7b0b2b5e   
    3  b2b6027bc5c5109e529d4dc6358b12c3  259dac757896d24d7702b9acbbff3f3c   
    4  4f2d8ab171c80ec8364f7c12e35b23ad  345ecd01c38d18a9036ed96c73b8d066   
    
       customer_zip_code_prefix          customer_city customer_state  
    0                     14409                 franca             SP  
    1                      9790  sao bernardo do campo             SP  
    2                      1151              sao paulo             SP  
    3                      8775        mogi das cruzes             SP  
    4                     13056               campinas             SP  
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 99441 entries, 0 to 99440
    Data columns (total 5 columns):
     #   Column                    Non-Null Count  Dtype 
    ---  ------                    --------------  ----- 
     0   customer_id               99441 non-null  object
     1   customer_unique_id        99441 non-null  object
     2   customer_zip_code_prefix  99441 non-null  int64 
     3   customer_city             99441 non-null  object
     4   customer_state            99441 non-null  object
    dtypes: int64(1), object(4)
    memory usage: 3.8+ MB
    None
    ---------------
    --- order-reviews ---
                              review_id                          order_id  \
    0  7bc2406110b926393aa56f80a40eba40  73fc7af87114b39712e6da79b0a377eb   
    1  80e641a11e56f04c1ad469d5645fdfde  a548910a1c6147796b98fdf73dbeba33   
    2  228ce5500dc1d8e020d8d1322874b6f0  f9e4b658b201a9f2ecdecbb34bed034b   
    3  e64fb393e7b32834bb789ff8bb30750e  658677c97b385a9be170737859d3511b   
    4  f7c4243c7fe1938f181bec41a392bdeb  8e6bfb81e283fa7e4f11123a3fb894f1   
    
       review_score review_comment_title  \
    0             4                  NaN   
    1             5                  NaN   
    2             5                  NaN   
    3             5                  NaN   
    4             5                  NaN   
    
                                  review_comment_message review_creation_date  \
    0                                                NaN  2018-01-18 00:00:00   
    1                                                NaN  2018-03-10 00:00:00   
    2                                                NaN  2018-02-17 00:00:00   
    3              Recebi bem antes do prazo estipulado.  2017-04-21 00:00:00   
    4  Parabéns lojas lannister adorei comprar pela I...  2018-03-01 00:00:00   
    
      review_answer_timestamp  
    0     2018-01-18 21:46:59  
    1     2018-03-11 03:05:13  
    2     2018-02-18 14:36:24  
    3     2017-04-21 22:02:06  
    4     2018-03-02 10:26:53  
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 99224 entries, 0 to 99223
    Data columns (total 7 columns):
     #   Column                   Non-Null Count  Dtype 
    ---  ------                   --------------  ----- 
     0   review_id                99224 non-null  object
     1   order_id                 99224 non-null  object
     2   review_score             99224 non-null  int64 
     3   review_comment_title     11568 non-null  object
     4   review_comment_message   40977 non-null  object
     5   review_creation_date     99224 non-null  object
     6   review_answer_timestamp  99224 non-null  object
    dtypes: int64(1), object(6)
    memory usage: 5.3+ MB
    None
    ---------------
    --- orders ---
                               order_id                       customer_id  \
    0  e481f51cbdc54678b7cc49136f2d6af7  9ef432eb6251297304e76186b10a928d   
    1  53cdb2fc8bc7dce0b6741e2150273451  b0830fb4747a6c6d20dea0b8c802d7ef   
    2  47770eb9100c2d0c44946d9cf07ec65d  41ce2a54c0b03bf3443c3d931a367089   
    3  949d5b44dbf5de918fe9c16f97b45f8a  f88197465ea7920adcdbec7375364d82   
    4  ad21c59c0840e6cb83a9ceb5573f8159  8ab97904e6daea8866dbdbc4fb7aad2c   
    
      order_status order_purchase_timestamp    order_approved_at  \
    0    delivered      2017-10-02 10:56:33  2017-10-02 11:07:15   
    1    delivered      2018-07-24 20:41:37  2018-07-26 03:24:27   
    2    delivered      2018-08-08 08:38:49  2018-08-08 08:55:23   
    3    delivered      2017-11-18 19:28:06  2017-11-18 19:45:59   
    4    delivered      2018-02-13 21:18:39  2018-02-13 22:20:29   
    
      order_delivered_carrier_date order_delivered_customer_date  \
    0          2017-10-04 19:55:00           2017-10-10 21:25:13   
    1          2018-07-26 14:31:00           2018-08-07 15:27:45   
    2          2018-08-08 13:50:00           2018-08-17 18:06:29   
    3          2017-11-22 13:39:59           2017-12-02 00:28:42   
    4          2018-02-14 19:46:34           2018-02-16 18:17:02   
    
      order_estimated_delivery_date  
    0           2017-10-18 00:00:00  
    1           2018-08-13 00:00:00  
    2           2018-09-04 00:00:00  
    3           2017-12-15 00:00:00  
    4           2018-02-26 00:00:00  
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 99441 entries, 0 to 99440
    Data columns (total 8 columns):
     #   Column                         Non-Null Count  Dtype 
    ---  ------                         --------------  ----- 
     0   order_id                       99441 non-null  object
     1   customer_id                    99441 non-null  object
     2   order_status                   99441 non-null  object
     3   order_purchase_timestamp       99441 non-null  object
     4   order_approved_at              99281 non-null  object
     5   order_delivered_carrier_date   97658 non-null  object
     6   order_delivered_customer_date  96476 non-null  object
     7   order_estimated_delivery_date  99441 non-null  object
    dtypes: object(8)
    memory usage: 6.1+ MB
    None
    ---------------
    --- order-payments ---
                               order_id  payment_sequential payment_type  \
    0  b81ef226f3fe1789b1e8b2acac839d17                   1  credit_card   
    1  a9810da82917af2d9aefd1278f1dcfa0                   1  credit_card   
    2  25e8ea4e93396b6fa0d3dd708e76c1bd                   1  credit_card   
    3  ba78997921bbcdc1373bb41e913ab953                   1  credit_card   
    4  42fdf880ba16b47b59251dd489d4441a                   1  credit_card   
    
       payment_installments  payment_value  
    0                     8          99.33  
    1                     1          24.39  
    2                     1          65.71  
    3                     8         107.78  
    4                     2         128.45  
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 103886 entries, 0 to 103885
    Data columns (total 5 columns):
     #   Column                Non-Null Count   Dtype  
    ---  ------                --------------   -----  
     0   order_id              103886 non-null  object 
     1   payment_sequential    103886 non-null  int64  
     2   payment_type          103886 non-null  object 
     3   payment_installments  103886 non-null  int64  
     4   payment_value         103886 non-null  float64
    dtypes: float64(1), int64(2), object(2)
    memory usage: 4.0+ MB
    None
    ---------------



```python
# Data preprocessing and cleaning
for name, df in loaded_data.items():
    # Handle missing values
    if df.isnull().sum().any():
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
        object_columns = df.select_dtypes(include=['object']).columns
        df[object_columns] = df[object_columns].fillna(df[object_columns].mode().iloc[0])

    # Remove duplicates
    df.drop_duplicates(inplace=True)


# Outlier detection and removal using Z-score
for name, df in loaded_data.items():
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        df = df[(np.abs(zscore(df[col])) < 3)]

# Normalization
for name, df in loaded_data.items():
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())


# Merge 'order_items' and 'orders' on 'order_id'
merged_df = pd.merge(loaded_data['order_items'], loaded_data['orders'], on='order_id')

# Merge the resulting DataFrame with 'customers' on 'customer_id'
final_df = pd.merge(merged_df, loaded_data['customers'], on='customer_id')

```


```python
# Feature engineering
order_items_df['total_cost'] = order_items_df['price'] + order_items_df['freight_value']


# Encoding categorical variables
for name, df in loaded_data.items():
    object_columns = df.select_dtypes(include=['object']).columns
    for col in object_columns:
        df[col] = df[col].astype('category').cat.codes

# Merge 'order_items' and 'orders' on 'order_id'
merged_df = pd.merge(loaded_data['order_items'], loaded_data['orders'], on='order_id')

# Merge the resulting DataFrame with 'customers' on 'customer_id'
final_df = pd.merge(merged_df, loaded_data['customers'], on='customer_id')


# Define a threshold for the minimum number of purchases
min_product_purchases = 10
min_customer_purchases = 10

# Filter out products that have been bought less than min_product_purchases times
product_counts = final_df['product_id'].value_counts()
popular_products = product_counts[product_counts >= min_product_purchases].index
final_df = final_df[final_df['product_id'].isin(popular_products)]

# Filter out customers who have bought less than min_customer_purchases times
customer_counts = final_df['customer_unique_id'].value_counts()
active_customers = customer_counts[customer_counts >= min_customer_purchases].index
final_df = final_df[final_df['customer_unique_id'].isin(active_customers)]

# Create user-item matrix
user_item_matrix = final_df.pivot_table(index='customer_unique_id', columns='product_id', values='total_cost')

# Fill missing values with 0
user_item_matrix.fillna(0, inplace=True)

# Print the user-item matrix
print(user_item_matrix)

```

    product_id             468       700       1633      3199      5158   \
    customer_unique_id                                                     
    2256                0.000000  0.000000  0.000000  0.000000  0.000000   
    5673                0.000000  0.000000  0.000000  0.000000  0.000000   
    17377               0.000000  0.000000  0.000000  0.000000  0.000000   
    18876               0.000000  0.000000  0.000000  0.000000  0.000000   
    36364               0.000000  0.000000  0.000000  0.000000  0.000000   
    36943               0.000000  0.000000  0.000000  0.000000  0.000000   
    51435               0.000000  0.000000  0.000000  0.000000  0.000000   
    54797               0.000000  0.000000  0.000000  0.033532  0.000000   
    57152               0.000000  0.000000  0.000000  0.000000  0.000000   
    57495               0.000000  0.000000  0.000000  0.000000  0.000000   
    69223               0.000000  0.000000  0.000000  0.000000  0.000000   
    70677               0.000000  0.000000  0.083372  0.000000  0.000000   
    72001               0.042271  0.000000  0.000000  0.000000  0.000000   
    79107               0.000000  0.019311  0.000000  0.000000  0.019311   
    80281               0.000000  0.000000  0.000000  0.000000  0.000000   
    85426               0.000000  0.000000  0.000000  0.000000  0.000000   
    
    product_id             6138      6620      7131      7267      8613   ...  \
    customer_unique_id                                                    ...   
    2256                0.000000  0.059854  0.000000  0.000000  0.000000  ...   
    5673                0.000000  0.000000  0.048193  0.000000  0.000000  ...   
    17377               0.084208  0.000000  0.000000  0.000000  0.000000  ...   
    18876               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    36364               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    36943               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    51435               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    54797               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    57152               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    57495               0.000000  0.000000  0.000000  0.010376  0.000000  ...   
    69223               0.000000  0.000000  0.000000  0.000000  0.041417  ...   
    70677               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    72001               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    79107               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    80281               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    85426               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    
    product_id             8937      10840     17709     19178     21302  \
    customer_unique_id                                                     
    2256                0.000000  0.000000  0.000000  0.000000  0.000000   
    5673                0.000000  0.000000  0.000000  0.000000  0.000000   
    17377               0.000000  0.055793  0.000000  0.000000  0.000000   
    18876               0.000000  0.000000  0.000000  0.049777  0.000000   
    36364               0.000000  0.000000  0.000000  0.000000  0.000000   
    36943               0.000000  0.000000  0.000000  0.000000  0.000000   
    51435               0.000000  0.000000  0.049191  0.000000  0.000000   
    54797               0.000000  0.000000  0.000000  0.000000  0.000000   
    57152               0.000000  0.000000  0.000000  0.000000  0.053795   
    57495               0.000000  0.000000  0.000000  0.000000  0.000000   
    69223               0.000000  0.000000  0.000000  0.000000  0.000000   
    70677               0.000000  0.000000  0.000000  0.000000  0.000000   
    72001               0.000000  0.000000  0.000000  0.000000  0.000000   
    79107               0.000000  0.000000  0.000000  0.000000  0.000000   
    80281               0.023318  0.000000  0.000000  0.000000  0.000000   
    85426               0.000000  0.000000  0.000000  0.000000  0.000000   
    
    product_id             27072     27232     27544     28327     30667  
    customer_unique_id                                                    
    2256                0.000000  0.000000  0.000000  0.000000  0.000000  
    5673                0.000000  0.000000  0.000000  0.000000  0.000000  
    17377               0.000000  0.000000  0.000000  0.000000  0.000000  
    18876               0.000000  0.000000  0.000000  0.000000  0.000000  
    36364               0.000000  0.000000  0.115084  0.000000  0.000000  
    36943               0.000000  0.000000  0.000000  0.000000  0.039426  
    51435               0.000000  0.000000  0.000000  0.000000  0.000000  
    54797               0.003144  0.000000  0.000000  0.047467  0.000000  
    57152               0.000000  0.000000  0.000000  0.000000  0.000000  
    57495               0.000000  0.000000  0.000000  0.000000  0.000000  
    69223               0.000000  0.000000  0.000000  0.000000  0.000000  
    70677               0.000000  0.000000  0.000000  0.000000  0.000000  
    72001               0.000000  0.000000  0.000000  0.000000  0.000000  
    79107               0.000000  0.000000  0.000000  0.000000  0.000000  
    80281               0.000000  0.000000  0.000000  0.000000  0.000000  
    85426               0.000000  0.022366  0.000000  0.000000  0.000000  
    
    [16 rows x 21 columns]



```python
# Fill missing values with 0
user_item_matrix.fillna(0, inplace=True)

# Print the user-item matrix
print(user_item_matrix)

# Print the first 5 rows of each DataFrame
for name, df in loaded_data.items():
    print(f"--- First 5 rows of {name} ---")
    print(df.head())
    print("\n")

# Print the summary statistics of each DataFrame
for name, df in loaded_data.items():
    print(f"--- Summary statistics of {name} ---")
    print(df.describe())
    print("\n")

# Print the number of missing values in each DataFrame
for name, df in loaded_data.items():
    print(f"--- Missing values in {name} ---")
    print(df.isnull().sum())
    print("\n")

```

    product_id             468       700       1633      3199      5158   \
    customer_unique_id                                                     
    2256                0.000000  0.000000  0.000000  0.000000  0.000000   
    5673                0.000000  0.000000  0.000000  0.000000  0.000000   
    17377               0.000000  0.000000  0.000000  0.000000  0.000000   
    18876               0.000000  0.000000  0.000000  0.000000  0.000000   
    36364               0.000000  0.000000  0.000000  0.000000  0.000000   
    36943               0.000000  0.000000  0.000000  0.000000  0.000000   
    51435               0.000000  0.000000  0.000000  0.000000  0.000000   
    54797               0.000000  0.000000  0.000000  0.033532  0.000000   
    57152               0.000000  0.000000  0.000000  0.000000  0.000000   
    57495               0.000000  0.000000  0.000000  0.000000  0.000000   
    69223               0.000000  0.000000  0.000000  0.000000  0.000000   
    70677               0.000000  0.000000  0.083372  0.000000  0.000000   
    72001               0.042271  0.000000  0.000000  0.000000  0.000000   
    79107               0.000000  0.019311  0.000000  0.000000  0.019311   
    80281               0.000000  0.000000  0.000000  0.000000  0.000000   
    85426               0.000000  0.000000  0.000000  0.000000  0.000000   
    
    product_id             6138      6620      7131      7267      8613   ...  \
    customer_unique_id                                                    ...   
    2256                0.000000  0.059854  0.000000  0.000000  0.000000  ...   
    5673                0.000000  0.000000  0.048193  0.000000  0.000000  ...   
    17377               0.084208  0.000000  0.000000  0.000000  0.000000  ...   
    18876               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    36364               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    36943               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    51435               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    54797               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    57152               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    57495               0.000000  0.000000  0.000000  0.010376  0.000000  ...   
    69223               0.000000  0.000000  0.000000  0.000000  0.041417  ...   
    70677               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    72001               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    79107               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    80281               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    85426               0.000000  0.000000  0.000000  0.000000  0.000000  ...   
    
    product_id             8937      10840     17709     19178     21302  \
    customer_unique_id                                                     
    2256                0.000000  0.000000  0.000000  0.000000  0.000000   
    5673                0.000000  0.000000  0.000000  0.000000  0.000000   
    17377               0.000000  0.055793  0.000000  0.000000  0.000000   
    18876               0.000000  0.000000  0.000000  0.049777  0.000000   
    36364               0.000000  0.000000  0.000000  0.000000  0.000000   
    36943               0.000000  0.000000  0.000000  0.000000  0.000000   
    51435               0.000000  0.000000  0.049191  0.000000  0.000000   
    54797               0.000000  0.000000  0.000000  0.000000  0.000000   
    57152               0.000000  0.000000  0.000000  0.000000  0.053795   
    57495               0.000000  0.000000  0.000000  0.000000  0.000000   
    69223               0.000000  0.000000  0.000000  0.000000  0.000000   
    70677               0.000000  0.000000  0.000000  0.000000  0.000000   
    72001               0.000000  0.000000  0.000000  0.000000  0.000000   
    79107               0.000000  0.000000  0.000000  0.000000  0.000000   
    80281               0.023318  0.000000  0.000000  0.000000  0.000000   
    85426               0.000000  0.000000  0.000000  0.000000  0.000000   
    
    product_id             27072     27232     27544     28327     30667  
    customer_unique_id                                                    
    2256                0.000000  0.000000  0.000000  0.000000  0.000000  
    5673                0.000000  0.000000  0.000000  0.000000  0.000000  
    17377               0.000000  0.000000  0.000000  0.000000  0.000000  
    18876               0.000000  0.000000  0.000000  0.000000  0.000000  
    36364               0.000000  0.000000  0.115084  0.000000  0.000000  
    36943               0.000000  0.000000  0.000000  0.000000  0.039426  
    51435               0.000000  0.000000  0.000000  0.000000  0.000000  
    54797               0.003144  0.000000  0.000000  0.047467  0.000000  
    57152               0.000000  0.000000  0.000000  0.000000  0.000000  
    57495               0.000000  0.000000  0.000000  0.000000  0.000000  
    69223               0.000000  0.000000  0.000000  0.000000  0.000000  
    70677               0.000000  0.000000  0.000000  0.000000  0.000000  
    72001               0.000000  0.000000  0.000000  0.000000  0.000000  
    79107               0.000000  0.000000  0.000000  0.000000  0.000000  
    80281               0.000000  0.000000  0.000000  0.000000  0.000000  
    85426               0.000000  0.022366  0.000000  0.000000  0.000000  
    
    [16 rows x 21 columns]
    --- First 5 rows of order_items ---
       order_id  order_item_id  product_id  seller_id  shipping_limit_date  \
    0         0            0.0        8628        854                24066   
    1         1            0.0       29597       2678                 7193   
    2         2            0.0       25667       1117                45695   
    3         3            0.0       15322       1919                89768   
    4         4            0.0       22079       2697                 1640   
    
          price  freight_value  total_cost  
    0  0.008620       0.032440    0.026085  
    1  0.035498       0.048648    0.054445  
    2  0.029425       0.043619    0.047137  
    3  0.001803       0.031219    0.020794  
    4  0.029558       0.044278    0.047659  
    
    
    --- First 5 rows of products ---
       product_id  product_category_name  product_name_lenght  \
    0        4053                     62             0.492958   
    1        7645                      3             0.549296   
    2       19351                     32             0.577465   
    3       26672                      9             0.309859   
    4       20305                     72             0.450704   
    
       product_description_lenght  product_photos_qty  product_weight_g  \
    0                    0.070963            0.000000          0.005566   
    1                    0.068205            0.000000          0.024737   
    2                    0.061685            0.000000          0.003810   
    3                    0.064443            0.000000          0.009177   
    4                    0.099799            0.157895          0.015461   
    
       product_length_cm  product_height_cm  product_width_cm  
    0           0.091837           0.077670          0.071429  
    1           0.234694           0.155340          0.125000  
    2           0.112245           0.067961          0.080357  
    3           0.193878           0.019417          0.178571  
    4           0.132653           0.145631          0.062500  
    
    
    --- First 5 rows of customers ---
       customer_id  customer_unique_id  customer_zip_code_prefix  customer_city  \
    0         2610               50396                  0.135432           1382   
    1         9561               15433                  0.088769           3428   
    2        30460                2272                  0.001495           3597   
    3        69605               14192                  0.078515           2341   
    4        30707               19733                  0.121763            707   
    
       customer_state  
    0              25  
    1              25  
    2              25  
    3              25  
    4              25  
    
    
    --- First 5 rows of order-reviews ---
       review_id  order_id  review_score  review_comment_title  \
    0      47621     44692          0.75                  2954   
    1      49619     63412          1.00                  2954   
    2      13223     96304          1.00                  2954   
    3      88592     39089          1.00                  2954   
    4      95219     54600          1.00                  2954   
    
       review_comment_message  review_creation_date  review_answer_timestamp  
    0                   14549                   411                    45069  
    1                   14549                   461                    56478  
    2                   14549                   440                    51510  
    3                   25691                   145                     5857  
    4                   20731                   452                    54423  
    
    
    --- First 5 rows of orders ---
       order_id  customer_id  order_status  order_purchase_timestamp  \
    0     88950        61760             3                     27601   
    1     32545        68729             3                     90667   
    2     27769        25513             3                     94565   
    3     57385        96583             3                     35022   
    4     67043        53773             3                     55221   
    
       order_approved_at  order_delivered_carrier_date  \
    0              26908                         24734   
    1              83753                         76467   
    2              86885                         78217   
    3              33878                         31485   
    4              52141                         49662   
    
       order_delivered_customer_date  order_estimated_delivery_date  
    0                          25874                            212  
    1                          88741                            411  
    2                          91782                            427  
    3                          33914                            251  
    4                          50231                            298  
    
    
    --- First 5 rows of order-payments ---
       order_id  payment_sequential  payment_type  payment_installments  \
    0     71445                 0.0             1              0.333333   
    1     65632                 0.0             1              0.041667   
    2     14656                 0.0             1              0.041667   
    3     72395                 0.0             1              0.333333   
    4     25966                 0.0             1              0.083333   
    
       payment_value  
    0       0.007269  
    1       0.001785  
    2       0.004809  
    3       0.007888  
    4       0.009401  
    
    
    --- Summary statistics of order_items ---
                order_id  order_item_id     product_id      seller_id  \
    count  112650.000000  112650.000000  112650.000000  112650.000000   
    mean    49301.469214       0.009892   16425.005841    1513.868398   
    std     28466.663741       0.035256    9454.271946     896.071239   
    min         0.000000       0.000000       0.000000       0.000000   
    25%     24624.250000       0.000000    8350.000000     784.000000   
    50%     49281.500000       0.000000   16223.000000    1509.000000   
    75%     73934.750000       0.000000   24620.750000    2360.000000   
    max     98665.000000       1.000000   32950.000000    3094.000000   
    
           shipping_limit_date          price  freight_value     total_cost  
    count        112650.000000  112650.000000  112650.000000  112650.000000  
    mean          47114.221056       0.017790       0.048795       0.042886  
    std           26638.772065       0.027269       0.038582       0.036671  
    min               0.000000       0.000000       0.000000       0.000000  
    25%           24369.250000       0.005799       0.031927       0.025630  
    50%           47542.500000       0.011010       0.039690       0.033220  
    75%           69834.750000       0.019906       0.051626       0.046854  
    max           93317.000000       1.000000       1.000000       1.000000  
    
    
    --- Summary statistics of products ---
             product_id  product_category_name  product_name_lenght  \
    count  32951.000000            32951.00000         32951.000000   
    mean   16475.000000               35.84043             0.612351   
    std     9512.278697               22.30599             0.142964   
    min        0.000000                0.00000             0.000000   
    25%     8237.500000               13.00000             0.521127   
    50%    16475.000000               32.00000             0.647887   
    75%    24712.500000               54.00000             0.732394   
    max    32950.000000               72.00000             1.000000   
    
           product_description_lenght  product_photos_qty  product_weight_g  \
    count                32951.000000        32951.000000      32951.000000   
    mean                     0.192451            0.062578          0.056313   
    std                      0.157776            0.090559          0.105922   
    min                      0.000000            0.000000          0.000000   
    25%                      0.085256            0.000000          0.007421   
    50%                      0.150451            0.000000          0.017316   
    75%                      0.239970            0.105263          0.047001   
    max                      1.000000            1.000000          1.000000   
    
           product_length_cm  product_height_cm  product_width_cm  
    count       32951.000000       32951.000000      32951.000000  
    mean            0.243011           0.145026          0.153542  
    std             0.172591           0.132399          0.107845  
    min             0.000000           0.000000          0.000000  
    25%             0.112245           0.058252          0.080357  
    50%             0.183673           0.106796          0.125000  
    75%             0.316327           0.184466          0.214286  
    max             1.000000           1.000000          1.000000  
    
    
    --- Summary statistics of customers ---
            customer_id  customer_unique_id  customer_zip_code_prefix  \
    count  99441.000000        99441.000000              99441.000000   
    mean   49720.000000        48051.265383                  0.344838   
    std    28706.288396        27727.905493                  0.301029   
    min        0.000000            0.000000                  0.000000   
    25%    24860.000000        24050.000000                  0.104499   
    50%    49720.000000        48042.000000                  0.236526   
    75%    74580.000000        72060.000000                  0.584895   
    max    99440.000000        96095.000000                  1.000000   
    
           customer_city  customer_state  
    count   99441.000000    99441.000000  
    mean     2379.012188       18.650456  
    std      1211.858246        7.080432  
    min         0.000000        0.000000  
    25%      1273.000000       12.000000  
    50%      2729.000000       22.000000  
    75%      3566.000000       25.000000  
    max      4118.000000       26.000000  
    
    
    --- Summary statistics of order-reviews ---
              review_id      order_id  review_score  review_comment_title  \
    count  99224.000000  99224.000000  99224.000000          99224.000000   
    mean   49202.018322  49320.858341      0.771605           2894.159528   
    std    28403.962609  28485.934262      0.336895            500.407870   
    min        0.000000      0.000000      0.000000              0.000000   
    25%    24603.750000  24639.750000      0.750000           2954.000000   
    50%    49201.500000  49310.500000      1.000000           2954.000000   
    75%    73796.250000  73989.250000      1.000000           2954.000000   
    max    98409.000000  98672.000000      1.000000           4526.000000   
    
           review_comment_message  review_creation_date  review_answer_timestamp  
    count            99224.000000          99224.000000             99224.000000  
    mean             16126.255180            406.723625             49050.540726  
    std               7042.491431            150.111399             28353.836202  
    min                  0.000000              0.000000                 0.000000  
    25%              14549.000000            296.000000             24478.750000  
    50%              14549.000000            426.000000             49046.500000  
    75%              14549.000000            528.000000             73581.250000  
    max              36158.000000            635.000000             98247.000000  
    
    
    --- Summary statistics of orders ---
               order_id   customer_id  order_status  order_purchase_timestamp  \
    count  99441.000000  99441.000000  99441.000000              99441.000000   
    mean   49720.000000  49720.000000      3.054424              49442.294888   
    std    28706.288396  28706.288396      0.485649              28533.436046   
    min        0.000000      0.000000      0.000000                  0.000000   
    25%    24860.000000  24860.000000      3.000000              24735.000000   
    50%    49720.000000  49720.000000      3.000000              49441.000000   
    75%    74580.000000  74580.000000      3.000000              74144.000000   
    max    99440.000000  99440.000000      7.000000              98874.000000   
    
           order_approved_at  order_delivered_carrier_date  \
    count       99441.000000                  99441.000000   
    mean        46528.589375                  44465.994087   
    std         26090.873532                  24459.277390   
    min             0.000000                      0.000000   
    25%         24228.000000                  22705.000000   
    50%         47164.000000                  46350.000000   
    75%         69175.000000                  67574.000000   
    max         90732.000000                  81017.000000   
    
           order_delivered_customer_date  order_estimated_delivery_date  
    count                   99441.000000                   99441.000000  
    mean                    46372.610613                     276.289448  
    std                     28397.743955                     101.970093  
    min                         0.000000                       0.000000  
    25%                     21602.000000                     202.000000  
    50%                     46316.000000                     291.000000  
    75%                     70999.000000                     358.000000  
    max                     95663.000000                     458.000000  
    
    
    --- Summary statistics of order-payments ---
                order_id  payment_sequential   payment_type  payment_installments  \
    count  103886.000000       103886.000000  103886.000000         103886.000000   
    mean    49674.769632            0.003310       0.991106              0.118890   
    std     28724.968002            0.025235       0.839946              0.111960   
    min         0.000000            0.000000       0.000000              0.000000   
    25%     24804.250000            0.000000       1.000000              0.041667   
    50%     49633.500000            0.000000       1.000000              0.041667   
    75%     74597.750000            0.000000       1.000000              0.166667   
    max     99439.000000            1.000000       4.000000              1.000000   
    
           payment_value  
    count  103886.000000  
    mean        0.011278  
    std         0.015917  
    min         0.000000  
    25%         0.004156  
    50%         0.007318  
    75%         0.012576  
    max         1.000000  
    
    
    --- Missing values in order_items ---
    order_id               0
    order_item_id          0
    product_id             0
    seller_id              0
    shipping_limit_date    0
    price                  0
    freight_value          0
    total_cost             0
    dtype: int64
    
    
    --- Missing values in products ---
    product_id                    0
    product_category_name         0
    product_name_lenght           0
    product_description_lenght    0
    product_photos_qty            0
    product_weight_g              0
    product_length_cm             0
    product_height_cm             0
    product_width_cm              0
    dtype: int64
    
    
    --- Missing values in customers ---
    customer_id                 0
    customer_unique_id          0
    customer_zip_code_prefix    0
    customer_city               0
    customer_state              0
    dtype: int64
    
    
    --- Missing values in order-reviews ---
    review_id                  0
    order_id                   0
    review_score               0
    review_comment_title       0
    review_comment_message     0
    review_creation_date       0
    review_answer_timestamp    0
    dtype: int64
    
    
    --- Missing values in orders ---
    order_id                         0
    customer_id                      0
    order_status                     0
    order_purchase_timestamp         0
    order_approved_at                0
    order_delivered_carrier_date     0
    order_delivered_customer_date    0
    order_estimated_delivery_date    0
    dtype: int64
    
    
    --- Missing values in order-payments ---
    order_id                0
    payment_sequential      0
    payment_type            0
    payment_installments    0
    payment_value           0
    dtype: int64
    
    



```python
# Frequency: count the number of purchases for each product
product_frequency = final_df['product_id'].value_counts()

# Central tendency: calculate the mean and median total cost
mean_cost = final_df['total_cost'].mean()
median_cost = final_df['total_cost'].median()

# Distribution: calculate the standard deviation of the total cost
std_dev_cost = final_df['total_cost'].std()

# Relationship: calculate the correlation between total cost and product_id
# Note: this requires product_id to be a numeric type. If it's a categorical type, you'll need to convert it to numeric.
correlation = final_df['total_cost'].corr(final_df['product_id'])

print(f"Product Frequency:\n{product_frequency}\n")
print(f"Mean Total Cost: {mean_cost}")
print(f"Median Total Cost: {median_cost}")
print(f"Standard Deviation of Total Cost: {std_dev_cost}")
print(f"Correlation between Total Cost and Product ID: {correlation}")
```

    Product Frequency:
    product_id
    22112    527
    19742    488
    8613     484
    7364     392
    7079     388
            ... 
    28334      1
    12122      1
    1484       1
    21105      1
    6906       1
    Name: count, Length: 32951, dtype: int64
    
    Mean Total Cost: 0.042885993734036953
    Median Total Cost: 0.03321956658707655
    Standard Deviation of Total Cost: 0.03667099040088164
    Correlation between Total Cost and Product ID: 0.010798755076964435



```python
import random

# Select specific product_ids
product_ids = [1633, 27232, 6138]  # replace with your chosen product_ids

# Select the total cost data for these products
product1 = final_df[final_df['product_id'] == product_ids[0]]['total_cost']
product2 = final_df[final_df['product_id'] == product_ids[1]]['total_cost']
product3 = final_df[final_df['product_id'] == product_ids[2]]['total_cost']

# Perform ANOVA
f_val, p_val = stats.f_oneway(product1, product2, product3)
print(f"F-value: {f_val}")
print(f"P-value: {p_val}")

# Sample the dataframe
sample_size = min(len(product1), len(product2), len(product3))  # Set sample size to the smallest product data length

sampled_df = final_df.sample(n=sample_size, random_state=42)  # Change random_state if desired

# Create a contingency table based on the sampled data
contingency_table = pd.crosstab(sampled_df['product_id'], sampled_df['customer_unique_id'])

# Perform Chi-square test on the sampled data
chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)
print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p_val}")

# Correlation with price on sampled data
correlation_price = sampled_df['total_cost'].corr(sampled_df['price'])
print(f"Correlation with Price: {correlation_price}")

# Correlation with freight_value on sampled data
correlation_freight = sampled_df['total_cost'].corr(sampled_df['freight_value'])
print(f"Correlation with Freight Value: {correlation_freight}")

# Prepare data from sampled products
sampled_product_data = pd.concat([product1.sample(n=sample_size, random_state=42),
                                  product2.sample(n=sample_size, random_state=42),
                                  product3.sample(n=sample_size, random_state=42)])
sampled_groups = ['product1'] * sample_size + ['product2'] * sample_size + ['product3'] * sample_size
sampled_df = pd.DataFrame({'values': sampled_product_data, 'groups': sampled_groups})

# Perform Dunn's test on sampled data
posthoc = sp.posthoc_dunn(sampled_df, val_col='values', group_col='groups', p_adjust='bonferroni')
print(posthoc)

```

    F-value: 93.93655601562766
    P-value: 2.0278910533148584e-16
    Chi-square statistic: 89.99999999999996
    P-value: 0.23134171389514194
    Correlation with Price: 0.747299115226813
    Correlation with Freight Value: 0.9382709969061643
              product1  product2  product3
    product1  1.000000  0.001586  1.000000
    product2  0.001586  1.000000  0.000053
    product3  1.000000  0.000053  1.000000



```python
# Histogram for 'total_cost'
plt.figure(figsize=(10, 6))
plt.hist(final_df['total_cost'], bins=30, edgecolor='black')
plt.title('Total Cost Distribution')
plt.xlabel('Total Cost')
plt.ylabel('Frequency')
plt.show()

# Boxplot for 'total_cost'
plt.figure(figsize=(10, 6))
sns.boxplot(final_df['total_cost'])
plt.title('Total Cost Boxplot')
plt.show()

# Scatter plot for 'total_cost' vs 'price'
plt.figure(figsize=(10, 6))
plt.scatter(final_df['total_cost'], final_df['price'])
plt.title('Total Cost vs Price')
plt.xlabel('Total Cost')
plt.ylabel('Price')
plt.show()

# Scatter plot for 'total_cost' vs 'freight_value'
plt.figure(figsize=(10, 6))
plt.scatter(final_df['total_cost'], final_df['freight_value'])
plt.title('Total Cost vs Freight Value')
plt.xlabel('Total Cost')
plt.ylabel('Freight Value')
plt.show()

# Heatmap for the correlation matrix of the DataFrame
plt.figure(figsize=(10, 6))
sns.heatmap(final_df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()


print(final_df.columns)

```


    
![png](output_12_0.png)
    



    
![png](output_12_1.png)
    



    
![png](output_12_2.png)
    



    
![png](output_12_3.png)
    



    
![png](output_12_4.png)
    


    Index(['order_id', 'order_item_id', 'product_id', 'seller_id',
           'shipping_limit_date', 'price', 'freight_value', 'total_cost',
           'customer_id', 'order_status', 'order_purchase_timestamp',
           'order_approved_at', 'order_delivered_carrier_date',
           'order_delivered_customer_date', 'order_estimated_delivery_date',
           'customer_unique_id', 'customer_zip_code_prefix', 'customer_city',
           'customer_state'],
          dtype='object')



```python
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Check for missing values and impute them
missing_values = final_df.isnull().sum()
print("Missing values per column:\n", missing_values)

# Impute missing values
for column in final_df.columns:
    if final_df[column].dtype == 'object':  # Categorical data
        final_df[column] = final_df[column].fillna(final_df[column].mode()[0])
    else:  # Numerical data
        final_df[column] = final_df[column].fillna(final_df[column].median())

# Confirm that there are no more missing values
print("\nMissing values after imputation:\n", final_df.isnull().sum())


# Data transformation
numerical_cols = final_df.select_dtypes(include=[np.number]).columns
final_df[numerical_cols] = final_df[numerical_cols].apply(zscore)

# Print the first 5 rows of the DataFrame to confirm transformations
print("\nFirst 5 rows after transformations:\n", final_df.head())


# Create user-item interaction matrix
interaction_matrix = final_df.pivot_table(index='customer_id', columns='product_id', values='order_item_id', fill_value=0, aggfunc='count')


# Print unique customer IDs
print(interaction_matrix.index.unique())



# Calculate item-item similarity matrix
item_similarity = cosine_similarity(interaction_matrix.T)
item_similarity = pd.DataFrame(item_similarity, index=interaction_matrix.columns, columns=interaction_matrix.columns)

# Function to get the most similar items
def get_similar_items(product_id, n=5):
    similar_items = item_similarity[product_id].sort_values(ascending=False)[:n+1]
    similar_items = similar_items.index[similar_items.index != product_id]  # Exclude the item itself
    return similar_items

# Function to recommend items for a user
def recommend_items(user_id, n=5):
    if user_id not in interaction_matrix.index:
        print(f"No data available for user ID: {user_id}")
        return []
    user_items = interaction_matrix.loc[user_id]
    not_interacted_items = user_items[user_items == 0].index
    item_scores = item_similarity[not_interacted_items].sum(axis=1)
    recommended_items = item_scores.nlargest(n)
    return recommended_items.index


# Get recommendations for a specific user
recommended_items = recommend_items(-1.9176302812675063)
print(f"Recommended items for user '-1.9176302812675063': {recommended_items}")


```

    Missing values per column:
     order_id                         0
    order_item_id                    0
    product_id                       0
    seller_id                        0
    shipping_limit_date              0
    price                            0
    freight_value                    0
    total_cost                       0
    customer_id                      0
    order_status                     0
    order_purchase_timestamp         0
    order_approved_at                0
    order_delivered_carrier_date     0
    order_delivered_customer_date    0
    order_estimated_delivery_date    0
    customer_unique_id               0
    customer_zip_code_prefix         0
    customer_city                    0
    customer_state                   0
    dtype: int64
    
    Missing values after imputation:
     order_id                         0
    order_item_id                    0
    product_id                       0
    seller_id                        0
    shipping_limit_date              0
    price                            0
    freight_value                    0
    total_cost                       0
    customer_id                      0
    order_status                     0
    order_purchase_timestamp         0
    order_approved_at                0
    order_delivered_carrier_date     0
    order_delivered_customer_date    0
    order_estimated_delivery_date    0
    customer_unique_id               0
    customer_zip_code_prefix         0
    customer_city                    0
    customer_state                   0
    dtype: int64
    
    First 5 rows after transformations:
        order_id  order_item_id  product_id  seller_id  shipping_limit_date  \
    0 -1.731910      -0.280567   -0.824711  -0.736405            -0.865217   
    1 -1.731874      -0.280567    1.393238   1.299156            -1.498620   
    2 -1.731839      -0.280567    0.977551  -0.442900            -0.053277   
    3 -1.731804      -0.280567   -0.116668   0.452122             1.601199   
    4 -1.731769      -0.280567    0.598039   1.320360            -1.707077   
    
          price  freight_value  total_cost  customer_id  order_status  \
    0 -0.336289      -0.423901   -0.458171    -0.909226     -0.110283   
    1  0.649372      -0.003816    0.315205     1.611678     -0.110283   
    2  0.426646      -0.134144    0.115930    -0.378179     -0.110283   
    3 -0.586298      -0.455534   -0.602449     1.158154     -0.110283   
    4  0.431547      -0.117062    0.130159    -0.535840     -0.110283   
    
       order_purchase_timestamp  order_approved_at  order_delivered_carrier_date  \
    0                 -0.858845          -0.851653                     -0.889802   
    1                 -1.465280          -1.500205                     -1.521421   
    2                 -0.043439          -0.023553                     -0.036223   
    3                  1.581177           1.546548                      1.396334   
    4                 -1.682407          -1.729941                     -1.743953   
    
       order_delivered_customer_date  order_estimated_delivery_date  \
    0                      -0.812599                      -0.745533   
    1                      -1.373949                      -1.695305   
    2                      -0.057310                       0.076949   
    3                       1.556604                       1.369421   
    4                      -1.560714                      -2.077171   
    
       customer_unique_id  customer_zip_code_prefix  customer_city  customer_state  
    0            0.095623                 -0.238276      -1.354932       -0.094444  
    1            1.451663                 -0.649073       0.747463        0.895317  
    2           -0.971724                  0.018447       0.233416       -1.225599  
    3            0.646438                 -0.743833      -1.693230        0.895317  
    4           -0.367554                 -0.734636       1.356399        0.895317  


    /tmp/ipykernel_151494/273660071.py:31: PerformanceWarning: The following operation may generate 3251143366 cells in the resulting pandas object.
      interaction_matrix = final_df.pivot_table(index='customer_id', columns='product_id', values='order_item_id', fill_value=0, aggfunc='count')



    ---------------------------------------------------------------------------

    MemoryError                               Traceback (most recent call last)

    Cell In[31], line 31
         27 print("\nFirst 5 rows after transformations:\n", final_df.head())
         30 # Create user-item interaction matrix
    ---> 31 interaction_matrix = final_df.pivot_table(index='customer_id', columns='product_id', values='order_item_id', fill_value=0, aggfunc='count')
         34 # Print unique customer IDs
         35 print(interaction_matrix.index.unique())


    File ~/.pyenv/versions/3.9.0/lib/python3.9/site-packages/pandas/core/frame.py:8579, in DataFrame.pivot_table(self, values, index, columns, aggfunc, fill_value, margins, dropna, margins_name, observed, sort)
       8562 @Substitution("")
       8563 @Appender(_shared_docs["pivot_table"])
       8564 def pivot_table(
       (...)
       8575     sort: bool = True,
       8576 ) -> DataFrame:
       8577     from pandas.core.reshape.pivot import pivot_table
    -> 8579     return pivot_table(
       8580         self,
       8581         values=values,
       8582         index=index,
       8583         columns=columns,
       8584         aggfunc=aggfunc,
       8585         fill_value=fill_value,
       8586         margins=margins,
       8587         dropna=dropna,
       8588         margins_name=margins_name,
       8589         observed=observed,
       8590         sort=sort,
       8591     )


    File ~/.pyenv/versions/3.9.0/lib/python3.9/site-packages/pandas/core/reshape/pivot.py:97, in pivot_table(data, values, index, columns, aggfunc, fill_value, margins, dropna, margins_name, observed, sort)
         94     table = concat(pieces, keys=keys, axis=1)
         95     return table.__finalize__(data, method="pivot_table")
    ---> 97 table = __internal_pivot_table(
         98     data,
         99     values,
        100     index,
        101     columns,
        102     aggfunc,
        103     fill_value,
        104     margins,
        105     dropna,
        106     margins_name,
        107     observed,
        108     sort,
        109 )
        110 return table.__finalize__(data, method="pivot_table")


    File ~/.pyenv/versions/3.9.0/lib/python3.9/site-packages/pandas/core/reshape/pivot.py:209, in __internal_pivot_table(data, values, index, columns, aggfunc, fill_value, margins, dropna, margins_name, observed, sort)
        207         else:
        208             to_unstack.append(name)
    --> 209     table = agged.unstack(to_unstack)
        211 if not dropna:
        212     if isinstance(table.index, MultiIndex):


    File ~/.pyenv/versions/3.9.0/lib/python3.9/site-packages/pandas/core/frame.py:8961, in DataFrame.unstack(self, level, fill_value)
       8899 """
       8900 Pivot a level of the (necessarily hierarchical) index labels.
       8901 
       (...)
       8957 dtype: float64
       8958 """
       8959 from pandas.core.reshape.reshape import unstack
    -> 8961 result = unstack(self, level, fill_value)
       8963 return result.__finalize__(self, method="unstack")


    File ~/.pyenv/versions/3.9.0/lib/python3.9/site-packages/pandas/core/reshape/reshape.py:475, in unstack(obj, level, fill_value)
        473 if isinstance(obj, DataFrame):
        474     if isinstance(obj.index, MultiIndex):
    --> 475         return _unstack_frame(obj, level, fill_value=fill_value)
        476     else:
        477         return obj.T.stack(dropna=False)


    File ~/.pyenv/versions/3.9.0/lib/python3.9/site-packages/pandas/core/reshape/reshape.py:504, in _unstack_frame(obj, level, fill_value)
        502     return obj._constructor(mgr)
        503 else:
    --> 504     return unstacker.get_result(
        505         obj._values, value_columns=obj.columns, fill_value=fill_value
        506     )


    File ~/.pyenv/versions/3.9.0/lib/python3.9/site-packages/pandas/core/reshape/reshape.py:213, in _Unstacker.get_result(self, values, value_columns, fill_value)
        210 if value_columns is None and values.shape[1] != 1:  # pragma: no cover
        211     raise ValueError("must pass column labels for multi-column data")
    --> 213 values, _ = self.get_new_values(values, fill_value)
        214 columns = self.get_new_columns(value_columns)
        215 index = self.new_index


    File ~/.pyenv/versions/3.9.0/lib/python3.9/site-packages/pandas/core/reshape/reshape.py:264, in _Unstacker.get_new_values(self, values, fill_value)
        262     else:
        263         dtype, fill_value = maybe_promote(dtype, fill_value)
    --> 264         new_values = np.empty(result_shape, dtype=dtype)
        265         new_values.fill(fill_value)
        267 name = dtype.name


    MemoryError: Unable to allocate 24.2 GiB for an array with shape (98666, 32951) and data type float64



```python

```
