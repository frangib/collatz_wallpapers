# Wallpapers
The [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) can produce very interesting visual patterns with little effort.

![drawing_1000v_0 2261206170954665](https://user-images.githubusercontent.com/44316116/139435945-86b7116a-2a7a-4758-8b47-710184f8238c.png)

# How to:
- Run conj.py
- Run conj_draw.py

# conj.py
- Must be run first to generate a CSV file containing the number of steps for every seed.
- N is the maximum seed value for which the number of steps is counted.
- The number of steps is computed as follows:
```
For example:
seed = 5
5 is odd   --> next =3x5+1 = 16
16 is even --> next = 16/2 = 8
8 is even  --> next = 8/2 = 4
4 is even  --> next = 4/2 = 2
2 is even  --> next = 2/2 = 1
next = 1   --> END
counter = 5
```

#conj_draw.py
- Must be run after conj.py
- **N must be smaller or equal than the value of N used in conj.py**
- The resolution (and ratio) of the resulting image can be modified changing HEIGHT and WIDTH.


# Examples:

![drawing_1000v_0 8261981732614936](https://user-images.githubusercontent.com/44316116/139436001-db3237a7-e97e-4b12-956a-2f912db09b9b.png)
![drawing_1000v_0 30377762610000036](https://user-images.githubusercontent.com/44316116/139435832-58523de4-e385-4845-880f-c8113ae3c29d.png)
![drawing_100v_0 16193512349207728](https://user-images.githubusercontent.com/44316116/139435836-b6aa24a5-a67b-4643-a815-017c552ffe2b.png)
![drawing_200v_0 8164414495988548](https://user-images.githubusercontent.com/44316116/139435840-8081cb08-e9f4-4507-9c6c-3dbddaafc37a.png)
![drawing_1000v_0 9332937686376698](https://user-images.githubusercontent.com/44316116/139435842-1b1f8c10-5d33-4728-9ad4-78d971fa7e30.png)
![drawing_1000v_0 28181988486650744](https://user-images.githubusercontent.com/44316116/139435848-e0321f7e-2030-4875-848b-31ad1f57fe37.png)

