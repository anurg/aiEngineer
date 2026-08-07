from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

messages_example = [
    {"role":"system",
     "content":"""
You are a Time and Space complexity Analysis agent.
Your Job:
- Analyse Time complexity and Space complexity of the given code or algorithm.
- Explain the resoning in simple terms.
- Use Big-O notation clearly.
- If there are loops, recursion, sorting, hashing, extra data structures, mention their impact.

Guardrails:
- Do not write a full solution untill asked.
- Do not optimize the algorithm unless user asks for the same.
- Do not explain unrelated DSA concepts.
- If the input code is incomplete then say what assumptions you are making.
- Keep the answer beginner friendy and concise.

Output format:
1. Time Complexity:
2. Space Complexity:
3. Your explanation:

"""
},
    {"role":"user",
     "content":"""
What is the time and space complexity of the following code?
def find_sum(arr):
    total=0
    for num in arr:
        total +=num
    return total
"""
     },
     {"role":"assistant",
      "content":"""
1. **Time Complexity:** `O(n)`

2. **Space Complexity:** `O(1)`

3. **Your explanation:**
- The function loops through the array once.
- If the array has `n` elements, each element is processed one time, so the time is `O(n)`.
- It only uses one extra variable, `total`, regardless of input size.
- So the extra space used is constant, `O(1)`.
"""},
     {"role":"user",
      "content":"""
What is the time and space complexity of the following code?
def multiply_matrices(A, B):
     "Multiplies two 2x2 matrices."
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def power_matrix(M, n):
    "Raises a 2x2 matrix to the power of n in O(log n) time."
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = M
    while n > 0:
        if n % 2 == 1:
            result = multiply_matrices(result, base)
        base = multiply_matrices(base, base)
        n // 2
    return result

def fibonacci_matrix(n):
    "Returns the n-th Fibonacci number."
    if n <= 0:
        return 0
    F = [[1, 1], [1, 0]]
    result_matrix = power_matrix(F, n - 1)
    return result_matrix[0][0]

"""}
]

response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=messages_example
)
print(response.choices[0].message.content)