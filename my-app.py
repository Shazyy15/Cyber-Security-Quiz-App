import tkinter as tk
from tkinter import messagebox, ttk
import random

def create_quiz_ui():
    def check_answer():
        nonlocal current_question, score
        user_answer = var.get()
        if user_answer == current_question["correct_answer"]:
            score += 1
        if len(answered_questions) < len(questions):
            display_question()
        else:
            show_result()

    def display_question():
        nonlocal current_question
        current_question = random.choice([q for q in questions if q not in answered_questions])
        answered_questions.append(current_question)
        question_label.config(text=f"Question {len(answered_questions)}/{len(questions)}:")
        question_text.config(state=tk.NORMAL)
        question_text.delete(1.0, tk.END)
        question_text.insert(tk.END, current_question['question'])
        question_text.config(state=tk.DISABLED)
        for i, option in enumerate(current_question["options"]):
            radio_buttons[i].config(text=option, value=i, background="#2C3E50")
        var.set(-1)  # Reset selection
        next_button.config(state=tk.DISABLED)
        progress['value'] = (len(answered_questions) / len(questions)) * 100

    def show_result():
        percentage = (score / len(questions)) * 100
        if percentage >= 80:
            knowledge_level = "Great"
            color = "#2ECC71"
        elif percentage >= 60:
            knowledge_level = "Normal"
            color = "#F39C12"
        else:
            knowledge_level = "Weak"
            color = "#E74C3C"
        
        result_window = tk.Toplevel(root)
        result_window.title("Quiz Result")
        result_window.geometry("400x300")
        result_window.configure(bg="#2C3E50")
        
        result_frame = ttk.Frame(result_window, padding="20", style="Result.TFrame")
        result_frame.pack(fill=tk.BOTH, expand=True)
        style.configure("Result.TFrame", background="#2C3E50")
        
        result_title = ttk.Label(result_frame, text="Quiz Completed!", font=("Arial", 20, "bold"), foreground="#ECF0F1", background="#2C3E50")
        result_title.pack(pady=10)
        
        score_label = ttk.Label(result_frame, text=f"Your score: {score}/{len(questions)}", font=("Arial", 16), foreground="#ECF0F1", background="#2C3E50")
        score_label.pack(pady=5)
        
        percentage_label = ttk.Label(result_frame, text=f"Percentage: {percentage:.2f}%", font=("Arial", 16), foreground="#ECF0F1", background="#2C3E50")
        percentage_label.pack(pady=5)
        
        knowledge_label = ttk.Label(result_frame, text=f"Your knowledge in cyber security is:", font=("Arial", 16), foreground="#ECF0F1", background="#2C3E50")
        knowledge_label.pack(pady=5)
        
        level_label = ttk.Label(result_frame, text=knowledge_level, font=("Arial", 24, "bold"), foreground=color, background="#2C3E50")
        level_label.pack(pady=10)
        
        close_button = ttk.Button(result_frame, text="Close", command=root.quit, style="Result.TButton")
        close_button.pack(pady=20)
        
        style.configure("Result.TButton", background=color, foreground="white")

    def enable_next_button():
        if var.get() != -1:
            next_button.config(state=tk.NORMAL)
        # Change background color of selected radio button to green
        for rb in radio_buttons:
            rb.config(background="#2C3E50")
        radio_buttons[var.get()].config(background="#2ECC71")

    root = tk.Tk()
    root.title("Cyber Security Quiz By Shazil Shahid")
    root.geometry("900x700")
    root.configure(bg="#2C3E50")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TButton", padding=10, relief="flat", background="#3498DB", foreground="white", font=("Arial", 12, "bold"))
    style.configure("TRadiobutton", background="#2C3E50", foreground="white", font=("Arial", 12))
    style.configure("TProgressbar", thickness=25, troughcolor="#34495E", background="#2ECC71")

    main_frame = ttk.Frame(root, padding="30", style="Main.TFrame")
    main_frame.pack(fill=tk.BOTH, expand=True)
    style.configure("Main.TFrame", background="#2C3E50")

    title_label = ttk.Label(main_frame, text="Cyber Security Quiz", font=("Arial", 24, "bold"), foreground="#ECF0F1", background="#2C3E50")
    title_label.pack(pady=20)

    question_label = ttk.Label(main_frame, text="", font=("Arial", 16, "bold"), foreground="#ECF0F1", background="#2C3E50")
    question_label.pack(pady=10)

    question_text = tk.Text(main_frame, wrap=tk.WORD, height=4, font=("Arial", 14), bg="#34495E", fg="#ECF0F1", relief=tk.FLAT)
    question_text.pack(pady=20, fill=tk.X)

    var = tk.IntVar()
    var.set(-1)

    radio_buttons = []
    for i in range(4):
        rb = tk.Radiobutton(main_frame, text="", variable=var, value=i, command=enable_next_button, 
                            bg="#2C3E50", fg="white", selectcolor="#2ECC71", font=("Arial", 12),
                            activebackground="#2ECC71", activeforeground="white")
        rb.pack(pady=10, padx=30, anchor=tk.W)
        radio_buttons.append(rb)

    next_button = tk.Button(main_frame, text="Next", command=check_answer, state=tk.DISABLED,
                            bg="#3498DB", fg="white", font=("Arial", 12, "bold"),
                            activebackground="#2ECC71", activeforeground="white")
    next_button.pack(pady=30)

    progress = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
    progress.pack(pady=20)

    developer_label = ttk.Label(main_frame, text="Developed by Shazil Shahid", font=("Arial", 10), foreground="#BDC3C7", background="#2C3E50")
    developer_label.pack(side=tk.BOTTOM, pady=10)

    current_question = None
    answered_questions = []
    score = 0

    questions = [
        {
            "question": "What is phishing?",
            "options": ["A fishing technique", "A type of cyber attack", "A programming language", "A network protocol"],
            "correct_answer": 1
        },
        {
            "question": "Which of the following is NOT a good password practice?",
            "options": ["Using uppercase and lowercase letters", "Using the same password for multiple accounts", "Including numbers and symbols", "Making the password at least 12 characters long"],
            "correct_answer": 1
        },
        {
            "question": "What does 'HTTPS' stand for?",
            "options": ["Hyper Text Transfer Protocol Secure", "High-Tech Transfer Protocol System", "Hyper Text Transmission Protocol Service", "Hybrid Text Transfer Protocol Standard"],
            "correct_answer": 0
        },
        {
            "question": "What is a firewall?",
            "options": ["A physical wall to protect servers", "A type of computer virus", "A security system that monitors network traffic", "A backup storage device"],
            "correct_answer": 2
        },
        {
            "question": "What is two-factor authentication?",
            "options": ["Using two different passwords", "Logging in from two devices", "Using a password and an additional verification method", "Changing your password twice a year"],
            "correct_answer": 2
        },
        {
            "question": "What is malware?",
            "options": ["Malicious hardware", "Malicious software", "A type of firewall", "A secure coding practice"],
            "correct_answer": 1
        },
        {
            "question": "What does VPN stand for?",
            "options": ["Very Private Network", "Virtual Private Network", "Visual Processing Node", "Verified Public Network"],
            "correct_answer": 1
        },
        {
            "question": "What is a DDoS attack?",
            "options": ["Distributed Denial of Service", "Data Deletion on Server", "Direct Database Override System", "Dynamic DNS Over SSL"],
            "correct_answer": 0
        },
        {
            "question": "What is encryption?",
            "options": ["Compressing data", "Deleting data", "Converting data into a code to prevent unauthorized access", "Backing up data"],
            "correct_answer": 2
        },
        {
            "question": "What is a zero-day vulnerability?",
            "options": ["A vulnerability that's been known for years", "A vulnerability with no risk", "A vulnerability known to the vendor but not yet patched", "A vulnerability discovered on day zero of a product's release"],
            "correct_answer": 3
        },
        {
            "question": "What is social engineering in cybersecurity?",
            "options": ["Building social networks securely", "Manipulating people to divulge confidential information", "Engineering social media platforms", "Creating secure social environments"],
            "correct_answer": 1
        },
        {
            "question": "What is a botnet?",
            "options": ["A network of robots", "A type of antivirus", "A network of infected computers controlled by an attacker", "A secure network protocol"],
            "correct_answer": 2
        },
        {
            "question": "What is ransomware?",
            "options": ["Software that protects against ransom demands", "Malware that encrypts files and demands payment for decryption", "A type of cryptocurrency", "A method of secure file transfer"],
            "correct_answer": 1
        },
        {
            "question": "What is a SQL injection attack?",
            "options": ["Injecting SQL databases with random data", "A method to optimize SQL queries", "Inserting malicious SQL code into application queries", "A technique to secure SQL databases"],
            "correct_answer": 2
        },
        {
            "question": "What is the purpose of a CAPTCHA?",
            "options": ["To make websites more colorful", "To slow down website loading", "To distinguish between humans and bots", "To compress web content"],
            "correct_answer": 2
        },
        {
            "question": "What is the principle of least privilege?",
            "options": ["Giving users the minimum levels of access they need to perform their job", "Providing all users with administrative access", "Restricting all user access", "Granting maximum privileges to all users"],
            "correct_answer": 0
        },
        {
            "question": "What is a man-in-the-middle attack?",
            "options": ["An attack on middle management", "An attack where the attacker secretly relays and possibly alters communication between two parties", "A type of social engineering attack", "An attack on network middle layers"],
            "correct_answer": 1
        },
        {
            "question": "What is the purpose of a honeypot in cybersecurity?",
            "options": ["To attract and trap hackers", "To store sensitive data", "To encrypt network traffic", "To speed up network connections"],
            "correct_answer": 0
        },
        {
            "question": "What is the difference between symmetric and asymmetric encryption?",
            "options": ["Symmetric uses one key, asymmetric uses two keys", "Symmetric is faster, asymmetric is slower", "Symmetric is less secure, asymmetric is more secure", "All of the above"],
            "correct_answer": 3
        },
        {
            "question": "What is the purpose of a security audit?",
            "options": ["To test network speed", "To evaluate and improve the security of an information system", "To increase system performance", "To reduce operational costs"],
            "correct_answer": 1
        }
    ]

    display_question()
    root.mainloop()

if __name__ == "__main__":
    create_quiz_ui()
