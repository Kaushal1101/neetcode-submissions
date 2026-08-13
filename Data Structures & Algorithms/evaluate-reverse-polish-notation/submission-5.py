class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["*", "/", "+", "-"]

        def perform_op(a, b, op):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "/":
                return int(a / b)
            else:
                return a * b
        
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                op2 = stack.pop()
                op1 = stack.pop()

                stack.append(perform_op(op1, op2, t))
        
        print(stack)
        return stack[0]