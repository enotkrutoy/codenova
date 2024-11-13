import streamlit as st
import os

# Инициализация истории сессий
if "recon_history" not in st.session_state:
    st.session_state.recon_history = []

# Заголовок приложения
st.title("WhiteRabbitNeo: Red Team Interface")

# Раздел для ввода IP-адреса или домена для разведки
st.header("Разведка цели")
target = st.text_input("Введите IP-адрес или домен цели:")

# Пример данных разведки
recon_data = f"""
- Цель: {target}
- IP-адрес: 192.168.1.1
- Открытые порты: 22, 80, 443
- Сервисы: SSH, HTTP, HTTPS
"""

# Кнопка для запуска разведки
if st.button("Запустить разведку"):
    if target:
        st.success("Разведка выполнена успешно!")
        st.subheader("Результаты разведки")
        st.code(recon_data, language="text")
    else:
        st.error("Пожалуйста, введите IP-адрес или домен.")

# Сохранение результатов разведки в файл
if st.button("Сохранить результаты разведки"):
    with open("recon_results.txt", "w") as f:
        f.write(recon_data)
    st.success("Результаты разведки сохранены в файл recon_results.txt")
    st.download_button(label="Скачать файл результатов разведки", data=recon_data, file_name="recon_results.txt", mime="text/plain")

# Сохранение результатов разведки в историю сессии
if st.button("Сохранить результаты в сессию"):
    st.session_state.recon_history.append(recon_data)
    st.success("Результаты разведки добавлены в историю сессии.")

# Отображение истории сессий
st.subheader("История разведки")
for idx, data in enumerate(st.session_state.recon_history):
    st.write(f"Сессия {idx+1}:")
    st.code(data, language="text")

# Пример кода эксплойта
st.header("Сгенерированный код эксплойта")
exploit_code = """
import socket

def exploit(target_ip, target_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    s.send(b"EXPLOIT_PAYLOAD")
    response = s.recv(1024)
    s.close()
    return response
"""

# Отображение сгенерированного кода эксплойта в формате Python
st.code(exploit_code, language="python")

# Кнопка для сохранения кода эксплойта в файл
if st.button("Сохранить код эксплойта"):
    with open("exploit_code.py", "w") as f:
        f.write(exploit_code)
    st.success("Код эксплойта сохранен в файл exploit_code.py")
    st.download_button(label="Скачать код эксплойта", data=exploit_code, file_name="exploit_code.py", mime="text/x-python")
