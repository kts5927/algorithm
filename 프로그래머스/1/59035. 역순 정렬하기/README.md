# [level 1] 역순 정렬하기 - 59035 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/59035) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > SELECT

### 채점결과

NAMEDATETIMERocky2016-06-07 09:17:00Shelly2015-01-29 15:01:00Benji2016-04-19 13:28:00Jackie2016-01-03 16:25:00*Sam2016-03-13 11:17:00Jimminee2015-07-28 18:17:00Mitty2014-06-21 12:25:00Raven2015-11-19 13:41:00Chewy2016-09-11 14:09:00Stanley2016-04-02 11:36:00Lizzie2014-12-25 12:02:00Jake2016-10-18 11:01:00Sabrina2016-05-12 20:23:00Kaila2014-05-16 14:17:00Anna2013-11-18 17:03:00Lucy2017-06-17 13:29:00Reggie2016-10-04 20:31:00Jack2013-10-14 15:38:00Lucy2015-08-25 14:08:00Charlie2017-07-12 14:43:00Raven2016-08-22 16:13:00Rogan2015-12-27 17:42:00Snickerdoodl2015-01-24 16:14:00Chip2015-07-26 11:39:00Skips2013-11-20 13:09:00Penny2014-01-31 13:46:00Nellie2017-03-16 16:53:00Rome2016-04-06 15:53:00Holly2013-12-08 17:04:00Blaze2015-11-27 15:59:00Spider2015-12-25 10:13:00Dakota2014-06-25 16:58:00Goldie2014-02-01 18:36:00Punch2015-08-17 12:55:00Tiko2015-12-19 12:52:00Giovanni2015-09-25 18:17:00Clyde2014-01-11 15:15:00Jedi2014-12-13 15:19:00Jj2014-07-04 01:55:00Finney2017-02-05 12:27:00Oreo2014-05-29 12:31:00Princess2014-11-08 16:14:00Maxwell 22015-03-13 13:14:00Cherokee2017-07-08 09:41:00Pepper2014-08-06 12:07:00Ruby2016-01-22 17:13:00Laika2017-08-04 16:45:00Scooby2014-02-03 12:41:00Pickle2016-02-01 14:35:00Disciple2013-10-23 11:42:00Mercedes2017-09-28 13:36:00Zoe2014-07-05 07:13:00Lyla2014-08-02 11:23:00Frijolito2014-01-25 14:38:00Lucy2017-10-25 17:17:00Dora2017-07-09 07:42:00Mama Dog2014-02-18 12:24:00Dash2015-06-12 12:47:00Rosie2014-03-20 12:31:00Ella2014-07-29 11:43:00April2016-06-07 17:42:00Sailor2015-05-11 12:33:00Ceballo2015-08-03 09:09:00Greg2015-07-29 16:07:00Katie2013-11-03 15:04:00Emily2014-10-27 14:43:00Sniket2016-06-25 11:46:002014-06-08 13:20:00Stormy2018-02-03 10:40:00Woody2014-10-19 14:49:00Cookie2015-09-10 16:01:00Miller2015-09-16 09:06:00Minnie2017-01-08 16:34:00Diablo2014-08-26 12:53:00Hugo2015-09-28 16:26:00Goofy2014-11-17 17:39:00Honey2014-06-08 18:19:00Girly Girl2016-01-27 12:27:00*Morado2016-04-21 08:19:00Stitch2014-11-18 21:20:00Baby Bear2015-03-30 11:36:00Simba2015-09-14 16:52:00Fuzzo2015-02-06 12:12:00Happy2016-03-17 14:09:00Puppy2016-03-11 15:43:00Queens2014-12-03 15:15:00Elijah2015-09-10 13:14:00Shadow2014-01-26 13:48:00Faith2015-05-08 18:34:00Sammy2017-04-21 11:33:00Kia2015-08-26 11:51:00Ariel2014-05-02 12:16:00Tux2014-12-11 11:48:00Bj2016-05-08 12:57:00Peanutbutter2015-07-09 17:51:00Gia2017-04-13 16:29:00Harley2014-08-08 04:20:00Meo2017-03-06 15:01:00Jewel2017-08-13 13:50:00Sugar2018-01-22 14:32:00

### 제출 일자

2025년 01월 04일 01:44:45

### 문제 설명

<p><code>ANIMAL_INS</code> 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. <code>ANIMAL_INS</code> 테이블 구조는 다음과 같으며, <code>ANIMAL_ID</code>, <code>ANIMAL_TYPE</code>, <code>DATETIME</code>, <code>INTAKE_CONDITION</code>, <code>NAME</code>, <code>SEX_UPON_INTAKE</code>는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>TYPE</th>
<th>NULLABLE</th>
</tr>
</thead>
        <tbody><tr>
<td>ANIMAL_ID</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>ANIMAL_TYPE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>DATETIME</td>
<td>DATETIME</td>
<td>FALSE</td>
</tr>
<tr>
<td>INTAKE_CONDITION</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>NAME</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
<tr>
<td>SEX_UPON_INTAKE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>DATETIME</th>
</tr>
</thead>
        <tbody><tr>
<td>Rocky</td>
<td>2016-06-07 09:17:00</td>
</tr>
<tr>
<td>Shelly</td>
<td>2015-01-29 15:01:00</td>
</tr>
<tr>
<td>Benji</td>
<td>2016-04-19 13:28:00</td>
</tr>
<tr>
<td>Jackie</td>
<td>2016-01-03 16:25:00</td>
</tr>
<tr>
<td>*Sam</td>
<td>2016-03-13 11:17:00</td>
</tr>
</tbody>
      </table>
<p>..이하 생략</p>

<hr>

<p>본 문제는 <a href="https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes" target="_blank" rel="noopener">Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"</a>에서 제공하는 데이터를 사용하였으며 <a href="https://opendatacommons.org/licenses/odbl/1.0/" target="_blank" rel="noopener">ODbL</a>의 적용을 받습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges