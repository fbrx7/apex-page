import curses

def main(stdscr):
    # إخفاء المؤشر في البداية
    curses.curs_set(1)  # تأكيد أن المؤشر مرئي
    
    # الحصول على أبعاد الشاشة
    height, width = stdscr.getmaxyx()
    
    # تقسيم الشاشة إلى قسمين: قسم الدردشة وقسم الأوامر
    chat_win = curses.newwin(height - 3, width, 0, 0)  # قسم الرسائل (الجزء العلوي)
    input_win = curses.newwin(3, width, height - 3, 0)  # قسم الأوامر (الجزء السفلي)
    
    chat_win.scrollok(True)  # السماح بالتمرير في قسم الدردشة
    input_win.keypad(True)  # تمكين الإدخال باستخدام المفاتيح

    # بعض النصوص لعرضها في قسم الدردشة
    chat_win.addstr(0, 0, "Welcome to the chat room!\n")
    chat_win.addstr(1, 0, "User1: Hello!\n")
    chat_win.addstr(2, 0, "User2: Hi, how are you?\n")
    
    # عرض قسم الدردشة
    chat_win.refresh()

    # الحلقة الرئيسية للتعامل مع الأوامر
    while True:
        # مسح قسم الأوامر عند كل تكرار للحلقة
        input_win.clear()  
        
        # إضافة نص ثابت في سطر الأوامر
        input_win.addstr(0, 0, "Enter command: ")

        # تحديث قسم الأوامر بشكل مستمر
        input_win.refresh()

        # قراءة الأوامر من المستخدم (كتابة النص في السطر)
        input_win.move(1, 0)  # تحريك المؤشر إلى السطر الثاني بعد النص الثابت
        command = input_win.getstr().decode('utf-8')  # قراءة النص المدخل من المستخدم
        
        # عند إدخال أمر "exit"، إنهاء البرنامج
        if command.lower() == "exit":
            break
        
        # إضافة الأمر المدخل إلى قسم الدردشة
        chat_win.addstr(f"Command entered: {command}\n")
        chat_win.refresh()  # تحديث قسم الدردشة بعد إضافة الأمر المدخل

# تشغيل الكود باستخدام curses
curses.wrapper(main)
