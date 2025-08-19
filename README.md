# LEetcode-solutions
You are given:  A 2D integer array ranges, where each ranges[i] = [startᵢ, endᵢ] represents an inclusive interval from startᵢ to endᵢ.  Two integers left and right.  Your task is to determine: 👉 Whether every integer in the inclusive range [left, right] is covered by at least one interval in ranges.


bool isCovered(int** ranges, int rangesSize, int* rangesColSize, int left, int right) {
    int watch[52] = {0};
    for (int i = 0; i < rangesSize; i++) {
        watch[ranges[i][0]]++;
        watch[ranges[i][1] + 1]--;
    }
    for (int i = 1; i < 52; i++) watch[i] += watch[i - 1];
    for (int i = left; i <= right; i++) if (watch[i] <= 0) return false;
    return true;
}
