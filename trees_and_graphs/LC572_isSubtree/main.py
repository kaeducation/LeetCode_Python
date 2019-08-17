class Solution():
    def isSubtree(self, s, t):

        def sametree(p, q):
            if p and q:
                return p.val == q.val and sametree(p.left, q.left) and sametree(p.right, q.right)
            return p == q

        stack = [s]

        while stack:
            popped = stack.pop()

            if sametree(popped, t):
                return True
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)

        return False
