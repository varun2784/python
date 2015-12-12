test cases:

1. Handle file if it does't exist
2. Handle duplicate by ignoring
3. Handle malformed user coordinates (float conversion fails)
4. Handle malformed shop coordinates (float conversion fails)
5. Handle if two or more shops have same coordinates( not handled)

Time Complexity

- Adding shop coordinates O(n)
- Sorting O(nlog(n))

Space Complexity
- Hash Table (O(n)) for finding duplicates based on name
- Distance Array for storing tuples (name, distance) - O(n)
