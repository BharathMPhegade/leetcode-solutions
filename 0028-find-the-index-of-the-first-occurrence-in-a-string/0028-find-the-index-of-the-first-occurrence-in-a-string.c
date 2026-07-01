int strStr(char* haystack, char* needle) {
    int j;
    int n = strlen(haystack);
    int m = strlen(needle);
    for(int i=0;i<=n-m;i++){
        for(j=0;j<m;j++){
            if(haystack[j+i] != needle[j]){
                break;
            }
        }
        if(j==m){
            return i;
        }
    }
    return -1;
}