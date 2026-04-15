import requests
from bs4 import BeautifulSoup

# 1. اللينك بتاع الموقع اللي هنسحب منه
url = "http://books.toscrape.com/"

# 2. بنبعت طلب (Request) للموقع عشان نفتح الصفحة
response = requests.get(url)

# بنطبع حالة الطلب (لو 200 يبقى كده نجحنا والموقع فتح)


# 3. بنحول كود الموقع (HTML) لشكل نقدر نقراه ونطلع منه الداتا
soup = BeautifulSoup(response.text, 'html.parser')

# هنجرب نطبع عنوان الصفحة (Title) عشان نتأكد إننا جوه الموقع صح








import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 1. بنقول لـ BeautifulSoup هات كل الكتب اللي في الصفحة
books = soup.find_all('article', class_='product_pod')

# هنعمل لستة فاضية عشان نخزن فيها بيانات الكتب
books_data = []

# 2. هنعمل لوب (Loop) عشان نعدي على كتاب كتاب ونطلع بياناته
for book in books:
    # استخراج اسم الكتاب (موجود جوه تاج a جوه h3)
    title = book.find('h3').find('a')['title']
    
    # استخراج السعر
    price = book.find('p', class_='price_color').text
    
    # استخراج التقييم (بيكون مكتوب كـ كلاس زي: star-rating Three)
    rating = book.find('p', class_='star-rating')['class'][1]
    
    # استخراج التوفر (In stock) مع تنظيف المسافات الزايدة بـ strip()
    availability = book.find('p', class_='instock availability').text.strip()
    
    # بنحط البيانات دي في قاموس (Dictionary) ونضيفها للستة بتاعتنا
    books_data.append({
        'Title': title,
        'Price': price,
        'Rating': rating,
        'Availability': availability
    })


    import pandas as pd

# --- الكود القديم بتاع السحب موجود فوق هنا ---

# 1. تحويل الداتا لجدول (DataFrame) باستخدام Pandas
df = pd.DataFrame(books_data)

# 2. تنظيف عمود السعر (Price)
# هنشيل علامة £ ونحول العمود لنوع Float (رقم عشري)
# استخدام Regex لاستخراج الأرقام والعلامة العشرية فقط
df['Price'] = df['Price'].str.extract(r'(\d+\.\d+)').astype(float)

# 3. تنظيف عمود التقييم (Rating)
# هنعمل قاموس صغير يحول الكلمات الإنجليزي لأرقام
ratings_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating'] = df['Rating'].map(ratings_dict)

# 4. حفظ البيانات النظيفة في ملف CSV
# بنعمل index=False عشان Pandas ميعملش عمود زيادة للترقيم
df.to_csv('Cleaned_Books_Data.csv', index=False, encoding='utf-8')

print("Success! Data has been cleaned and saved to Cleaned_Books_Data.csv")


import os
print("File saved exactly at:", os.path.abspath('Cleaned_Books_Data.csv'))