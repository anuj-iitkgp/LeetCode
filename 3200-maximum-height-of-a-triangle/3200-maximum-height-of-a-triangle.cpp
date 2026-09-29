#include <cmath>
#include <algorithm>

class Solution {
public:
    int maxHeightOfTriangle(int red, int blue) {
        auto calHeight = [](int c1, int c2) {
            int b = std::sqrt(c1);
            int r = (-1 + std::sqrt(1 + 4 * c2)) / 2;
            
            if (b > r) {
                return 2 * r + 1;
            } else {
                return 2 * b;
            }
        };

        return std::max(calHeight(red, blue), calHeight(blue, red));
    }
};