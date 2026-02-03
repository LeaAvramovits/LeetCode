class Solution {
public:
   #include <climits>


int reverse(int x) {
    long long res = 0; 
    while (x != 0) {
        int digit = x % 10;
        res = res * 10 + digit;
        if (res > INT_MAX || res < INT_MIN) return 0; 
        x /= 10;
    }
    return (int)res;
}

};