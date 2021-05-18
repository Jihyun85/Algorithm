# 시간복잡도 (Big O)

- 알고리즘의 성능을 수학적으로 표현해주는 표기법
- 알고리즘의 시간, 공간복잡도를 표현 가능
- 알고리즘의 실제 러닝타임보다는 데이터나 사용자 증가율에 따른 알고리즘 성능을 예측하는 것이 목표
- ⭐ Big O 표기법에서는 상수는 과감하게 버린다! ex. O(2n) => O(n)  
  → 이유 : **성능**을 예측하는 것이 목표이기 때문이다.

## 📖 O(1)

: 입력 데이터의 크기와 상관없이 언제나 일정한 시간이 걸리는 알고리즘

```javascript
const printFirst = (array) => console.log(array[0]);
```

## 📖 O(n)

: 입력 데이터의 크기에 비례해서 처리 시간이 걸리는 알고리즘

```javascript
const printNumbers = (array) => array.forEach((num) => console.log(num));
```

## 📖 O(n²)

: n개의 데이터를 두 번 도는 알고리즘

```javascript
function calculate(arr1) {
  let newArray = [];
  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr1.length; j++) {
      newArray.push(i + j);
    }
  }
}
```

## 📖 O(nm)

: O(n²)와 다른 점은 n개의 데이터를 두 번 도는 것이 아니라 n개의 데이터를 m만큼 돌게 된다.

```javascript
function calculate(arr1, arr2) {
  let newArray = [];
  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr2.length; j++) {
      newArray.push(i + j);
    }
  }
}
```

## 📖 O(n³)

: n개의 데이터를 3번 도는 알고리즘 (큐빅 모양)

```javascript
function calculate(arr1) {
  let newArray = [];
  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr1.length; j++) {
      for (let k = 0; k < arr1.length; k++) {
        newArray.push(i + j + k);
      }
    }
  }
}
```

## 📖 O(2ⁿ)

: 대표적인 예시 - 피보나치 수열

```javascript
function fibonacci(n, r) {
  if (n <= 0) return 0;
  else if (n == 1) return (r[n] = 1);
  return (r[n] = fibonacci(n - 1, r) + fibonacci(n - 2, r));
}
```

## 📖 O(log n)

: 한 번 처리가 진행될 때마다 검색해야 하는 데이터가 절반으로 떨어지는 알고리즘  
: 대표적인 예시 - 이진검색

> **이진검색**  
> : 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘.  
>  처음 중간의 값을 임의의 값으로 선택하여, 그 값과 찾고자 하는 값의 크고 작음을 비교하는 방식

```javascript
function binarySearch(key, array, start, end) {
  if (start > end) return -1;
  mid = (start + end) / 2;
  if (arr[mid] == k) return mid;
  else if (arr[mid] > k) return binarySearch(key, array, start, mid - 1);
  else return binarySearch(key, array, mid + 1, end);
}
```

## 📖 O(sqrt(n))

> square root : 제곱근

---

### 참고

- 유튜브 엔지니어대한민국: https://www.youtube.com/watch?v=6Iq5iMCVsXA
- (피보나치 수열 관련) : https://swtpumpkin.github.io/algorithm/level1/fibonacciNumber/
