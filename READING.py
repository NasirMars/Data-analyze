import datetime
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

total_pages = 200
begin_pages = 55
begining_date = "2024/07/31"
daily_pages_read_array = [5, 6, 7, 9, 12]

current_date = 0
pages_read = begin_pages
num_days = len(daily_pages_read_array)
date_array = []

def time(start_day, current_date):
    date_obj=datetime.datetime.strptime(start_day, "%Y/%m/%d").date()
    plan_date=date_obj+datetime.timedelta(days=current_date)
    return plan_date

if __name__=='__main__':
    for x in range(num_days):
      pages_read = pages_read + daily_pages_read_array[x]

    with tqdm(total=total_pages, ncols=160) as pbar:
        pbar.update(pages_read)
    print("\n")
    while current_date < num_days:
        plan_date = time(begining_date, current_date)
        date_array.append(plan_date.strftime('%Y/%m/%d'))
        current_date += 1
    # print(daily_pages_read_array)
    # print(date_array)
    plt.figure(figsize=(7, 7))
    # plt.xticks(rotation=25)
    plt.grid(True, which='both', linestyle=':', linewidth=1, color='red')
    plt.gca().yaxis.set_major_locator(MultipleLocator(1)) 
    plt.plot(date_array, daily_pages_read_array, marker='o')
    plt.ylim(0, max(daily_pages_read_array) + 1) 
    plt.xlabel("time")
    plt.ylabel("read pages")
    plt.title("READING CHART")
    plt.show()
