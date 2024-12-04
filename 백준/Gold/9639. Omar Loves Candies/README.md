# [Gold III] Omar Loves Candies - 9639 

[문제 링크](https://www.acmicpc.net/problem/9639) 

### 성능 요약

메모리: 144728 KB, 시간: 4736 ms

### 분류

누적 합

### 제출 일자

2024년 12월 4일 15:02:25

### 문제 설명

<p>Omar loves to eat a lot of candies, but unfortunately most of the candies are not healthy. So his parents found a way to give each candy a score, a higher score means a healthier candy (the score is an integer that can be positive, zero or negative).</p>

<p>One day he went with his parents to buy some candies, and they found a strange store where all the candies are stored in a 2-dimensional grid of N rows with M candies in each row. The rows are numbered from 1 to N from top to bottom, and the columns are numbered from 1 to M from left to right and every cell contains one candy.</p>

<p>They noticed something else, any candy (except for those in the first row) is healthier than the candy which is exactly above it, and any candy (except for those in the first column) is healthier than the candy which is exactly to its left (healthier means having higher score as defined above).</p>

<p>There is one more strange thing about this store, to buy some candies you have to select a sub-rectangle of the candies’ grid and buy all the candies within this sub-rectangle.</p>

<p>Omar’s parents want to select a non-empty sub-rectangle that has the maximum sum of candies’ scores among all possible sub-rectangles.</p>

<p>For example, consider the grid in the example input. Some of the possible sub-rectangles of candies they can select are [-2, -1, 2, 3], [-4, -2, -1] or [2, 3, 4, 5]. The last sub-rectangle has the maximum sum of scores, which is 14. They can not select the following lists of candies [1, 2, 3, 4, 5] or [-2, -1, 2] (because these lists do not form a sub-rectangle of the given grid).</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images2/omar.png" style="height:172px; width:170px"></p>

<p>Can you help them by writing a program which finds the non-empty sub-rectangle with the maximum possible sum of scores in the given grid?</p>

### 입력 

 <p>Your program will be tested on one or more test cases. The first line of the input will be a single integer T, the number of test cases (1 ≤ T ≤ 100). Followed by the test cases, each test case starts with a line containing two integers separated by a single space N M (1 ≤ N , M ≤ 1,000) representing the dimensions of the candies’ grid, followed by N lines, each one contains M integers separated by a single space, representing the candies’ scores in this row. The given grid representation will satisfy the conditions mentioned above, and each integer in the grid will not be less than -2,000 and will not be greater than 2,000.</p>

### 출력 

 <p>For each test case, print a single line which contains a single integer representing the maximum sum of scores they can get from a non-empty sub-rectangle.</p>

