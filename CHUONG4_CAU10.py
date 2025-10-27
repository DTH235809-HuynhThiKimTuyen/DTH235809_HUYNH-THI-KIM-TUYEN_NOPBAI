import time

# 4 hình mẫu (có thể thay bằng hình khác nếu đề cho cụ thể)
hinh1 = """
               *
               * * 
               ****
          **********
          * * *
          * *
          *
          

"""

hinh2 = """
*****
*    
**** 
*    
*****
"""

hinh3 = """
  ***  
 *   * 
*     *
*     *
 *   * 
  ***  
"""

hinh4 = """
*   *
*   *
*****
*   *
*   *
"""

# In lần lượt từng hình, mỗi hình cách nhau 5 giây
for hinh in [hinh1, hinh2, hinh3, hinh4]:
    print(hinh)
    time.sleep(5)
