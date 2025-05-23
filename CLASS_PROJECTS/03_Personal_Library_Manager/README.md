Assignment: Personal Library Manager
Objective

Create a command-line Personal Library Manager that allows users to manage their book collection. The program should let users add, remove, and search for books. Each book will be stored as a dictionary with details like title, author, publication year, genre, and read status. The program should also include a menu system, basic statistics, and optional file handling for saving and loading the library.
Requirements
Core Features

    Book Details: Each book should have the following attributes:
        Title (string)
        Author (string)
        Publication Year (integer)
        Genre (string)
        Read Status (boolean: True if read, False if unread)

    Menu System: Implement a menu with the following options:
        Add a book
        Remove a book
        Search for a book
        Display all books
        Display statistics (total books, percentage read)
        Exit

    Add a Book: Prompt the user to enter the book's details and add it to the library.

    Remove a Book: Prompt the user to enter the title of the book to remove it from the library.

    Search for a Book: Allow the user to search for a book by title or author. Display all matching books.

    Display All Books: Show all books in the library in a formatted way.

    Display Statistics:
        Total number of books in the library.
        Percentage of books that have been read.

    Exit: Exit the program.

Optional Challenge (File Handling)

    Save Library to a File: Save the library data to a file (e.g., library.txt) when the program exits.
    Load Library from a File: Load the library data from the file when the program starts.

Sample Output
Menu

Welcome to your Personal Library Manager!  
1. Add a book  
2. Remove a book  
3. Search for a book  
4. Display all books  
5. Display statistics  
6. Exit  
Enter your choice:  

Add a Book

Enter the book title: The Great Gatsby  
Enter the author: F. Scott Fitzgerald  
Enter the publication year: 1925  
Enter the genre: Fiction  
Have you read this book? (yes/no): yes  
Book added successfully!  

Remove a Book

Enter the title of the book to remove: The Great Gatsby  
Book removed successfully!  

Search for a Book

Search by:  
1. Title  
2. Author  
Enter your choice: 1  
Enter the title: The Great Gatsby  
Matching Books:  
1. The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read  

Display All Books

Your Library:  
1. The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read  
2. 1984 by George Orwell (1949) - Dystopian - Unread  

Display Statistics

Total books: 2  
Percentage read: 50.0%  

Exit

Library saved to file. Goodbye!  

Instructions

    Use a list of dictionaries to store the books.
    Use loops and conditionals to implement the menu system.
    Use string manipulation to format the output.
    Use type casting to convert user input to appropriate data types.
    (Optional) Use file handling to save and load the library.

Submission

    Write your code in a Python file named library_manager.py.
    Test your program thoroughly to ensure all features work as expected.
    (Optional) Include a text file (library.txt) to demonstrate file handling.

Tips

    Start by implementing the core features first.
    Test each feature individually before moving to the next.
    Use comments to explain your code.
    Have fun and be creative!

Once you are done submit this form ASAP:

https://forms.gle/tS7C3sr55tUZ36GY8

Good luck! 🚀


اسائنمنٹ: ذاتی لائبریری مینیجر
مقصد

ایک کمانڈ لائن پرسنل لائبریری مینیجر بنائیں جو صارفین کو اپنی کتابوں کے مجموعے کا انتظام کرنے کی اجازت دیتا ہے۔ پروگرام کو صارفین کو کتابیں شامل کرنے، ہٹانے اور تلاش کرنے کی اجازت دینی چاہیے۔ ہر کتاب کو عنوان، مصنف، اشاعت کا سال، صنف، اور پڑھنے کی حیثیت جیسی تفصیلات کے ساتھ ایک لغت کے طور پر ذخیرہ کیا جائے گا۔ پروگرام میں لائبریری کو محفوظ کرنے اور لوڈ کرنے کے لیے ایک مینو سسٹم، بنیادی اعدادوشمار، اور اختیاری فائل ہینڈلنگ بھی شامل ہونی چاہیے۔
تقاضے
بنیادی خصوصیات

    کتاب کی تفصیلات: ہر کتاب میں درج ذیل صفات ہونی چاہئیں۔
        عنوان (سٹرنگ)
        مصنف (سٹرنگ)
        اشاعت کا سال (عدد)
        نوع (سٹرنگ)
        پڑھنے کی حیثیت (بولین: صحیح اگر پڑھا جائے تو غلط، اگر پڑھا نہیں گیا تو غلط)

    مینو سسٹم: درج ذیل اختیارات کے ساتھ ایک مینو نافذ کریں:
        ایک کتاب شامل کریں۔
        ایک کتاب ہٹا دیں۔
        ایک کتاب تلاش کریں۔
        تمام کتابیں دکھائیں۔
        ڈسپلے کے اعداد و شمار (کل کتابیں، فیصد پڑھی گئی)
        باہر نکلیں۔

        اختیاری چیلنج (فائل ہینڈلنگ)

    لائبریری کو فائل میں محفوظ کریں: جب پروگرام ختم ہو جائے تو لائبریری ڈیٹا کو فائل میں محفوظ کریں (جیسے library.txt)۔
    فائل سے لائبریری لوڈ کریں: پروگرام شروع ہونے پر لائبریری کا ڈیٹا فائل سے لوڈ کریں۔

نمونہ آؤٹ پٹ
مینو

آپ کے ذاتی لائبریری مینیجر میں خوش آمدید!  
1. ایک کتاب شامل کریں۔  
2. ایک کتاب ہٹا دیں۔  
3. ایک کتاب تلاش کریں۔  
4. تمام کتابیں ڈسپلے کریں۔  
5. اعدادوشمار دکھائیں۔  
6. باہر نکلیں۔  
اپنی پسند درج کریں:  

ایک کتاب شامل کریں۔

کتاب کا عنوان درج کریں: دی گریٹ گیٹسبی  
مصنف درج کریں: ایف سکاٹ فٹزجیرالڈ  
اشاعت کا سال درج کریں: 1925  
صنف درج کریں: افسانہ  
کیا آپ نے یہ کتاب پڑھی ہے؟ (ہاں/نہیں): ہاں  
کتاب کامیابی کے ساتھ شامل ہوگئی!  

ایک کتاب کو ہٹا دیں۔

ہٹانے کے لیے کتاب کا عنوان درج کریں: دی گریٹ گیٹسبی  
کتاب کامیابی کے ساتھ ہٹا دی گئی!  

ایک کتاب تلاش کریں۔

تلاش کریں بذریعہ:  
1. عنوان  
2. مصنف  
اپنی پسند درج کریں: 1  
عنوان درج کریں: دی گریٹ گیٹسبی  
مماثل کتابیں:  
1. دی گریٹ گیٹسبی از ایف سکاٹ فٹزجیرالڈ (1925) - افسانہ - پڑھیں  

تمام کتابیں ڈسپلے کریں۔

آپ کی لائبریری:  
1. دی گریٹ گیٹسبی از ایف سکاٹ فٹزجیرالڈ (1925) - افسانہ - پڑھیں  
2. جارج آرویل کی طرف سے 1984 (1949) - Dystopian - بغیر پڑھا ہوا  

اعدادوشمار دکھائیں۔

کل کتابیں: 2  
پڑھنے کا فیصد: 50.0%  

باہر نکلیں۔

لائبریری فائل میں محفوظ ہو گئی۔ الوداع!  

ہدایات

    کتابوں کو ذخیرہ کرنے کے لیے لغات کی فہرست استعمال کریں۔
    مینو سسٹم کو لاگو کرنے کے لیے لوپس اور مشروط استعمال کریں۔
    آؤٹ پٹ کو فارمیٹ کرنے کے لیے سٹرنگ ہیرا پھیری کا استعمال کریں۔
    صارف کے ان پٹ کو مناسب ڈیٹا کی اقسام میں تبدیل کرنے کے لیے ٹائپ کاسٹنگ کا استعمال کریں۔
    (اختیاری) لائبریری کو محفوظ کرنے اور لوڈ کرنے کے لیے فائل ہینڈلنگ کا استعمال کریں۔

    جمع کرانا

    library_manager.py نام کی ایک Python فائل میں اپنا کوڈ لکھیں۔
    اپنے پروگرام کی اچھی طرح جانچ کریں تاکہ یہ یقینی بنایا جا سکے کہ تمام خصوصیات توقع کے مطابق کام کرتی ہیں۔
    (اختیاری) فائل ہینڈلنگ کو ظاہر کرنے کے لیے ٹیکسٹ فائل (library.txt) شامل کریں۔

تجاویز

    پہلے بنیادی خصوصیات کو لاگو کرکے شروع کریں۔
    اگلے پر جانے سے پہلے ہر خصوصیت کو انفرادی طور پر جانچیں۔
    اپنے کوڈ کی وضاحت کے لیے تبصرے استعمال کریں۔
    مزہ کریں اور تخلیقی بنیں!

ایک بار جب آپ یہ فارم جمع کر لیں ASAP:

https://forms.gle/tS7C3sr55tUZ36GY8

گڈ لک! 🚀
