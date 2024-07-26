# Libraries
import pandas as pd
import numpy as np

# Inputs
mean_GBM = input.mean()                                           
vol_GBM = input_vol                                                 

T = 1                                                               
n = 12                                                             
W = 1000                                                            

dt = T / n                                                          

# Data Storage
all_results = {}                                                                               
price_proxy = pd.DataFrame(columns=['Date', 'Price Proxy'])                                    


# Algorithm
for date in input.index:  
  """ Looping through the input data frame """
    S0 = input.loc[date]                                                                        
    results = []                                                                                

    for i in range(1, W + 1):                                                                  
        St_m1 = S0                                                                              
        path = [St_m1]                                                                          

        for j in range(1, n + 1):
          """ Geometric Brownian Motion algorithm
              is based on Shonkwiler, R.W. (2013)) """
            Zt = np.random.normal()                                                             
            dST = St_m1 * (mean_GBM * dt + vol_GBM * np.sqrt(dt) * Zt)                          
            ST = St_m1 + dST                                                                    
            path.append(ST)                                                                     
            St_m1 = ST                                                                          
        results.append(path)                                                                    

    GBM_results = pd.DataFrame(results).T                                                       
    GBM_results.columns = [f'Path_{i}' for i in range(1, W + 1)]                                

    all_results[date] = GBM_results                                                             

    price_mean = GBM_results.iloc[-1].mean()                                                     
    price_proxy = price_proxy.append({'Date': date, 'Price Proxy': 
                                                  price_mean}, ignore_index=True);              

price_proxy.set_index('Date', inplace=True)                                                     


print(price_proxy)

