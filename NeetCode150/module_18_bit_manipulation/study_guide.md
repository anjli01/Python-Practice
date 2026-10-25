# Module 6.3: Bit Manipulation – Study Guide & Pattern Deep-Dive

Bit manipulation operates directly on binary representation, achieving **$O(1)$ auxiliary space and blazing fast hardware-level execution**.

---

## 1. Single Number (LeetCode 136) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/single-number/) • [NeetCode Problem](https://neetcode.io/problems/single-number) • [NeetCode Solution](https://neetcode.io/solutions/single-number) • [YouTube Video](https://www.youtube.com/watch?v=qMPX1AOa83k)
* **Pattern**: XOR Self-Cancellation
* **Core Concept**:
  $x \oplus x = 0$ and $x \oplus 0 = x$. Since XOR is commutative and associative, XOR-ing all elements causes every duplicate pair to cancel to zero, leaving only the lone single number. Order of operations doesn't matter.
* **Mental Model**:
  A light switch game. Every number flips a switch. Duplicates flip the same switch twice (returning it to off). The only switch left on at the end is the single number.
* **Tips & Interview Tricks**:
  * **One-Liner**: `return reduce(xor, nums)` or `result = 0; for n in nums: result ^= n`. This is the cleanest $O(n)$ time, $O(1)$ space solution possible.
  * **Why Not Hash Set?**: A hash set works in $O(n)$ time but uses $O(n)$ space. XOR achieves $O(1)$ space — always mention this trade-off.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 2. Number of 1 Bits (LeetCode 191) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/number-of-1-bits/) • [NeetCode Problem](https://neetcode.io/problems/number-of-one-bits) • [NeetCode Solution](https://neetcode.io/solutions/number-of-1-bits) • [YouTube Video](https://www.youtube.com/watch?v=5Km3utixwZs)
* **Pattern**: Brian Kernighan's Bit-Clearing
* **Core Concept**:
  The operation `n & (n - 1)` always clears the least significant set bit (the rightmost 1). The loop executes exactly as many times as there are 1-bits in $n$, making it strictly optimal.
* **Mental Model**:
  Popping bubbles. Each `n & (n - 1)` pops the rightmost bubble (1-bit). Count the pops until no bubbles remain.
* **Tips & Interview Tricks**:
  * **Why Not Shift and Check?**: `n & 1` followed by `n >>= 1` runs exactly 32 times (for 32-bit integers). Brian Kernighan's runs only $k$ times where $k$ is the number of set bits. For sparse numbers (few 1s), it's much faster.
  * **Built-In Alternative**: `bin(n).count('1')` works in Python. Mention it as a shortcut but demonstrate the bit manipulation approach.
* **Complexity**:
  * Time: $O(\text{set bits}) \le 32$
  * Space: $O(1)$

---

## 3. Counting Bits (LeetCode 338) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/counting-bits/) • [NeetCode Problem](https://neetcode.io/problems/counting-bits) • [NeetCode Solution](https://neetcode.io/solutions/counting-bits) • [YouTube Video](https://www.youtube.com/watch?v=RyBM56RIWrM)
* **Pattern**: Bit-Shift Subproblem DP
* **Core Concept**:
  $\text{dp}[i] = \text{dp}[i // 2] + (i\ \&\ 1) = \text{dp}[i \gg 1] + (i\ \&\ 1)$. Right-shifting by 1 gives a number already solved in the DP table; just add the parity of the current number (whether its last bit is 1).
* **Mental Model**:
  Every number is its "right-shifted parent" with an optional extra 1-bit tacked on the right. The parent's bit count is already known. Just check if the child added a 1 or a 0 at the end.
* **Tips & Interview Tricks**:
  * **Alternative Recurrence**: `dp[i] = dp[i & (i-1)] + 1` (Brian Kernighan-based). Each number's bit count is 1 more than the number with its lowest set bit cleared. Both recurrences are $O(n)$.
  * **$O(n)$ Guarantee**: The problem asks for a solution without using `__builtin_popcount` in a loop (which would be $O(n \log n)$). The DP approach achieves strict $O(n)$.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$ auxiliary (output array doesn't count)

---

## 4. Reverse Bits (LeetCode 190) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/reverse-bits/) • [NeetCode Problem](https://neetcode.io/problems/reverse-bits) • [NeetCode Solution](https://neetcode.io/solutions/reverse-bits) • [YouTube Video](https://www.youtube.com/watch?v=UcoN6UjAI64)
* **Pattern**: 32-Bit Reversal Accumulator
* **Core Concept**:
  Loop 32 times: shift `res` left by 1 and bitwise-OR the lowest bit of $n$: `res = (res << 1) | (n & 1)`, then shift $n$ right by 1: `n >>= 1`. After 32 iterations, `res` contains the reversed bit pattern.
* **Mental Model**:
  Reading a binary number backwards. Extract the rightmost bit of the input and place it as the next bit in the output, building the reversed number from left to right.
* **Tips & Interview Tricks**:
  * **Fixed 32 Iterations**: Always loop exactly 32 times, regardless of the input value. Leading zeros in the input become trailing zeros in the output and vice versa.
  * **Follow-Up (Multiple Calls)**: If called frequently, precompute a lookup table for 8-bit or 16-bit chunks. Reverse each chunk via table lookup and combine. This is $O(1)$ per call after initialization.
* **Complexity**:
  * Time: $O(1)$ (exactly 32 iterations)
  * Space: $O(1)$

---

## 5. Missing Number (LeetCode 268) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/missing-number/) • [NeetCode Problem](https://neetcode.io/problems/missing-number) • [NeetCode Solution](https://neetcode.io/solutions/missing-number) • [YouTube Video](https://www.youtube.com/watch?v=WnPLSRLSANE)
* **Pattern**: XOR Index-Value Reduction
* **Core Concept**:
  Initialize `res = n`. XOR every index $i$ and `nums[i]`: `res ^= i ^ nums[i]`. All numbers present in the array cancel out with their index counterpart (since $x \oplus x = 0$), leaving only the missing number.
* **Mental Model**:
  A roll call where every student's number is called alongside their seat number. XOR pairs them up. The student whose seat exists but whose name is never called is the missing number.
* **Tips & Interview Tricks**:
  * **Sum Formula Alternative**: Missing $= \frac{n(n+1)}{2} - \sum nums$. This is simpler but risks integer overflow in languages without arbitrary-precision integers. XOR never overflows.
  * **Why Initialize with $n$?**: Indices run from $0$ to $n-1$, but values include $n$. Initializing `res = n` accounts for the index $n$ that doesn't exist in the loop.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 6. Sum of Two Integers (LeetCode 371) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/sum-of-two-integers/) • [NeetCode Problem](https://neetcode.io/problems/sum-of-two-integers) • [NeetCode Solution](https://neetcode.io/solutions/sum-of-two-integers) • [YouTube Video](https://www.youtube.com/watch?v=gVUrDV4tZfY)
* **Pattern**: Bitwise Half-Adder with Carry Masking
* **Core Concept**:
  * Addition without carry: `a ^ b` (XOR gives the sum bits where carries aren't needed).
  * Carry bits: `(a & b) << 1` (AND identifies positions where both bits are 1, shifted left to propagate).
  * Repeat until carry is zero. In Python (due to arbitrary precision integers), apply `mask = 0xFFFFFFFF` to simulate 32-bit two's complement.
* **Mental Model**:
  A hardware adder circuit. XOR computes the partial sum. AND computes the carry. Feed the carry back into the adder and repeat until there's nothing left to carry — exactly how digital circuits add numbers.
* **Tips & Interview Tricks**:
  * **Python's Infinite Integers**: Python integers have arbitrary precision, so negative numbers don't naturally truncate to 32 bits. Use `mask = 0xFFFFFFFF` and apply `a &= mask; b &= mask` each iteration. At the end, if `a > 0x7FFFFFFF`, convert back: `a = ~(a ^ mask)`.
  * **Constant Iterations**: The loop runs at most 32 times (the carry can propagate at most 32 positions in a 32-bit integer).
* **Complexity**:
  * Time: $O(1)$ (at most 32 iterations)
  * Space: $O(1)$

---

## 7. Reverse Integer (LeetCode 7) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/reverse-integer/) • [NeetCode Problem](https://neetcode.io/problems/reverse-integer) • [NeetCode Solution](https://neetcode.io/solutions/reverse-integer) • [YouTube Video](https://www.youtube.com/watch?v=HAgLH58IgJQ)
* **Pattern**: Digit Reversal with 32-Bit Overflow Checks
* **Core Concept**:
  Extract digits using modulo 10 (`digit = x % 10; x = x // 10`) and construct the reversed integer (`res = res * 10 + digit`). Before each multiplication, check against signed 32-bit boundaries $[-2^{31}, 2^{31} - 1]$, returning 0 upon overflow.
* **Mental Model**:
  Popping digits off the end of a number like popping elements from a stack, then pushing them onto a new number. Each pop-and-push reverses the digit order.
* **Tips & Interview Tricks**:
  * **Overflow Check Before Multiply**: Check `if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7): return 0` BEFORE `res = res * 10 + digit`. The `7` comes from $2^{31} - 1 = 2147483647$ (last digit is 7).
  * **Python Modulo Gotcha**: In Python, `-123 % 10 = 7` (not `-3`), because Python's modulo always returns a non-negative result. Use `int(math.fmod(x, 10))` or handle sign separately.
  * **Sign Handling**: Extract the sign first, work with the absolute value, and reapply the sign at the end.
* **Complexity**:
  * Time: $O(\log_{10} x) \le 10$
  * Space: $O(1)$
