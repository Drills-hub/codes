# [Silver IV] 궁합 쌍 찾기 - 14911 

[문제 링크](https://www.acmicpc.net/problem/14911) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

자료 구조, 브루트포스 알고리즘, 정렬, 해시를 사용한 집합과 맵

### 제출 일자

2025년 6월 2일 15:42:28

### 문제 설명

<p>첫째 줄에 주어진 여러 개의 정수 중에서 합이 둘째 줄에 주어진 수와 같은 서로 다른 위치에 있는 두 수의 쌍을 모두 출력하고 맨 아래에 이 쌍의 개수를 이어서 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 빈 칸으로 구분된 정수가 2개 이상, 10개 이하 주어진다. 둘째 줄에는 정수가 하나 주어진다. 주어지는 정수는 100,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>찾은 수의 쌍을 한 줄에 하나씩 출력하고 맨 아랫 줄에 그러한 쌍의 개수를 출력한다.</p>

<p>구성은 같지만, 순서가 다른 쌍 (a, b)와 (b, a)는 쌍 하나로 하며, a ≤ b인 쌍을 출력한다.</p>

<p>쌍이 여러 개인 경우에는 사전 순으로 출력한다. (a, b)가 (c, d)보다 사전 순으로 앞서는 기준은 a < c이거나, a == c 이면서, b < d 인 것이다.</p>

