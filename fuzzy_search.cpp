using namespace std;

bool fuzzysearch(const string& s1, const string& s2 ) {
    long long l = 0;
    for (long long i = 0; i < s2.size(); i++) {
        if (s2[i] == s1[l]) {
            l++;
        }
        if (l == s1.size()) {
            return true;
        }
    }
    return false;
}
