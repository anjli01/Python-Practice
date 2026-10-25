# Module 6.3: Bit Manipulation – Study Guide & Pattern Deep-Dive

Bit manipulation operates directly on binary representation, achieving **$O(1)$ auxiliary space and blazing fast hardware-level execution**.

---

## 1. Single Number (LeetCode 136) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/single-number/) • [NeetCode Problem](https://neetcode.io/problems/single-number) • [NeetCode Solution](https://neetcode.io/solutions/single-number) • [YouTube Video](https://www.youtube.com/watch?v=qMPX1AOa83k)
* **Pattern**: XOR Self-Cancellation
* **Core Concept**:
  $x \oplus x = 0$ and $x \oplus 0 = x$. Since XOR is commutative and associative, pairing duplicate numbers reduces them to 0, leaving the lone single number.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 2. Number of 1 Bits (LeetCode 191) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/number-of-1-bits/) • [NeetCode Problem](https://neetcode.io/problems/number-of-one-bits) • [NeetCode Solution](https://neetcode.io/solutions/number-of-1-bits) • [YouTube Video](https://www.youtube.com/watch?v=5Km3utixwZs)
* **Pattern**: Brian Kernighan's Bit-Clearing
* **Core Concept**:
  The operation `n & (n - 1)` always clears the least significant set bit (the rightmost 1). The loop executes exactly as many times as there are 1s in $n$.
* **Complexity**: Time: $O(\text{set bits}) \le 32$, Space: $O(1)$.

---

## 3. Counting Bits (LeetCode 338) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/counting-bits/) • [NeetCode Problem](https://neetcode.io/problems/counting-bits) • [NeetCode Solution](https://neetcode.io/solutions/counting-bits) • [YouTube Video](https://www.youtube.com/watch?v=RyBM56RIWrM)
* **Pattern**: Bit-Shift Subproblem DP
* **Core Concept**:
  $\text{dp}[i] = \text{dp}[i // 2] + (i \& 1) = \text{dp}[i \gg 1] + (i \& 1)$. Right-shifting by 1 is already solved in the DP table; just add the parity of the current number.
* **Complexity**: Time: $O(n)$, Space: $O(1)$ auxiliary.

---

## 4. Reverse Bits (LeetCode 190) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/reverse-bits/) • [NeetCode Problem](https://neetcode.io/problems/reverse-bits) • [NeetCode Solution](https://neetcode.io/solutions/reverse-bits) • [YouTube Video](https://www.youtube.com/watch?v=UcoN6UjAI64)
* **Pattern**: 32-Bit Reversal Accumulator
* **Core Concept**:
  Loop 32 times: shift `res` left by 1 and bitwise-OR the lowest bit of $n$ (`res = (res << 1) | (n & 1)`), then shift $n$ right by 1 (`n >>= 1`).
* **Complexity**: Time: $O(1)$ (exactly 32 iterations), Space: $O(1)$.

---

## 5. Missing Number (LeetCode 268) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/missing-number/) • [NeetCode Problem](https://neetcode.io/problems/missing-number) • [NeetCode Solution](https://neetcode.io/solutions/missing-number) • [YouTube Video](https://www.youtube.com/watch?v=WnPLSRLSANE)
* **Pattern**: XOR Index-Value Reduction
* **Core Concept**:
  Initialize `res = n`. XOR every index $i$ and `nums[i]`: `res ^= i ^ nums[i]`. All numbers present in the array cancel out with their index counterpart, leaving only the missing number.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 6. Sum of Two Integers (LeetCode 371) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/sum-of-two-integers/) • [NeetCode Problem](https://neetcode.io/problems/sum-of-two-integers) • [NeetCode Solution](https://neetcode.io/solutions/sum-of-two-integers) • [YouTube Video](https://www.youtube.com/watch?v=gVUrDV4tZfY)
* **Pattern**: Bitwise Half-Adder with Carry Masking
* **Core Concept**:
  * Addition without carry: `a ^ b`
  * Carry bits: `(a & b) << 1`
  * Repeat until carry is zero. In Python (due to arbitrary precision integers), apply `mask = 0xFFFFFFFF` to simulate 32-bit two's complement.
* **Complexity**: Time: $O(1)$ (at most 32 additions), Space: $O(1)$.

---

## 7. Reverse Integer (LeetCode 7) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/reverse-integer/) • [NeetCode Problem](https://neetcode.io/problems/reverse-integer) • [NeetCode Solution](https://neetcode.io/solutions/reverse-integer) • [YouTube Video](https://www.youtube.com/watch?v=HAgLH58IgJQ)
* **Pattern**: Digit Reversal with 32-Bit Overflow Checks
* **Core Concept**:
  Extract digits using modulo 10 and construct reversed integer. Clamp against signed 32-bit boundaries $[-2^{31}, 2^{31} - 1]$, returning 0 upon overflow.
* **Complexity**: Time: $O(\log_{10} x) \le 10$, Space: $O(1)$.
