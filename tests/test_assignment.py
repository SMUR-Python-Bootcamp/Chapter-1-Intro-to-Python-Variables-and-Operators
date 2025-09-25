import runpy
import builtins
import pytest

def run_student_code():
    """
    Runs the student's assignment1.py file in a fresh namespace
    and captures its globals (variables).
    """
    return runpy.run_path("assignment1.py")

def test_task1_output(capsys):
    run_student_code()
    captured = capsys.readouterr().out.strip().splitlines()
    # Check first three printed lines
    assert captured[0] == "Hello, VIP SMUR!"
    assert captured[1] == "I'm excited to learn python!"
    assert captured[2] == "This is my first assignment."

def test_task2_variables_and_output(capsys):
    ns = run_student_code()
    assert "my_name" in ns
    assert "my_age" in ns
    assert "favorite_color" in ns
    assert isinstance(ns["my_name"], str)
    assert isinstance(ns["my_age"], int)
    assert isinstance(ns["favorite_color"], str)

    captured = capsys.readouterr().out
    assert f"Hi, my name is {ns['my_name']}" in captured
    assert f"I am {ns['my_age']} years old" in captured
    assert f"my favorite color is {ns['favorite_color']}" in captured

def test_task3_math_output(capsys):
    ns = run_student_code()
    assert "num1" in ns and "num2" in ns

    num1, num2 = ns["num1"], ns["num2"]
    captured = capsys.readouterr().out

    assert f"Addition: {num1 + num2}" in captured
    assert f"Subtraction: {num1 - num2}" in captured
    assert f"Multiplication: {num1 * num2}" in captured
    assert f"Division: {num1 / num2}" in captured

def test_task4_comparisons(capsys):
    ns = run_student_code()
    num1, num2 = ns["num1"], ns["num2"]
    captured = capsys.readouterr().out

    assert f"Is num1 greater than num2? {num1 > num2}" in captured
    assert f"Is num1 equal to num2? {num1 == num2}" in captured
    assert f"Is num1 not equal to num2? {num1 != num2}" in captured

def test_task5_score(capsys):
    ns = run_student_code()
    assert "score" in ns
    captured = capsys.readouterr().out
    assert "Final score:" in captured
    # Example: "Final score: 15"
    final_line = [line for line in captured.splitlines() if line.startswith("Final score:")][0]
    value = int(final_line.split(":")[1].strip())
    assert value == ns["score"]
