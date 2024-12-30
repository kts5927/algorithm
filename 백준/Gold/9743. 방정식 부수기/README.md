# [Gold III] 방정식 부수기 - 9743 

[문제 링크](https://www.acmicpc.net/problem/9743) 

### 성능 요약

메모리: 33948 KB, 시간: 4320 ms

### 분류

브루트포스 알고리즘, 구현, 수학

### 제출 일자

2024년 12월 30일 11:29:17

### 문제 설명

<p>집합 A = {a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ..., a<sub>n</sub>}, a<sub>i</sub> ∈ {0, 1, 2, 3, ...}과 여섯 방정식이 주어진다.</p>

<ul>
	<li>c<sub>1</sub> = x<sub>1</sub> + x<sub>2</sub></li>
	<li>x<sub>4</sub> = x<sub>3</sub> + x<sub>1</sub></li>
	<li>x<sub>5</sub> = x<sub>6</sub> + x<sub>7</sub></li>
	<li>x<sub>11</sub> = x<sub>8</sub> + x<sub>9</sub></li>
	<li>x<sub>6</sub> = x<sub>2</sub> + x<sub>10</sub></li>
	<li>x<sub>12</sub> = x<sub>9</sub> + c<sub>2</sub></li>
</ul>

<p>c<sub>1</sub>과 c<sub>2</sub>는 정수 상수이다. c<sub>1</sub>과 c<sub>2</sub>가 주어졌을 때, 방정식을 푸는 프로그램을 작성하시오. 즉, 모든 x<sub>i</sub>를 찾아야 한다. 또, 모든 x<sub>i</sub>는 A의 원소이어야 한다. 또, 항상 방정식을 풀 수 있는 경우만 입력으로 주어진다.</p>

### 입력 

 <p>첫째 줄에 n, c<sub>1</sub>, c<sub>2</sub>가 주어진다. 둘째 줄부터 n개 줄에는 a<sub>i</sub>가 주어진다. 12 ≤ n ≤ 7,000, a<sub>i</sub>는 32비트 정수이다.</p>

### 출력 

 <p>출력은 총 12줄이다. 첫 번째 줄에 x<sub>1</sub>, 두 번째 줄에 x<sub>2</sub>, ..., 열두 번째 줄에 x<sub>12</sub>를 출력한다.</p>

