class TimeComplexityAllInOne:
    def constant_time(self, n):
        result = n * 2
        print("O(1)")

    def logarithmic_time(self, n):
        i = 1
        while i < n:
            i *= 2
        print("O(log n)")

    def linear_time(self, n):
        for i in range(n):
            pass
        print("O(n)")

    def n_log_n_time(self, n):
        for i in range(n):
            j = 1
            while j < n:
                j *= 2
        print("O(n log n)")

    def quadratic_time(self, n):
        for i in range(n):
            for j in range(n):
                pass
        print("O(n^2)")

    def n_cross_m_time(self, n, m):
        for i in range(n):
            for j in range(m):
                pass
        print("O(n * m)")

    def exponential_time(self, n):
        if n <= 0:
            return
        self.exponential_time(n - 1)
        self.exponential_time(n - 1)


demo = TimeComplexityAllInOne()

demo.constant_time(100)
demo.logarithmic_time(100)
demo.linear_time(100)
demo.n_log_n_time(100)
demo.quadratic_time(100)
demo.n_cross_m_time(10, 20)

demo.exponential_time(4)
print("O(2^n)")