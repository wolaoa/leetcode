#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

    struct Interval {
      int start;
      int End;
      Interval() : start(0), End(0) {}
      Interval(int s, int e) : start(s), End(e) {}
  };
class Solution {
public:
    vector<Interval> merge(vector<Interval> &intervals) {
        int len = intervals.size();
        for(int i=0;i<len-1;i++)
        {
            for(int j=i+1;j<len;j++)
            {
                if(intervals[i].start>intervals[j].start)
                    swap(intervals[i],intervals[j]);
                else if(intervals[i].start == intervals[j].start)
                {
                    if(intervals[i].End>intervals[j].End)
                        swap(intervals[i],intervals[j]);
                }
            }
        }

        vector<Interval> ans;
        int j=0;
        ans.push_back(intervals[j]);
        for(j=1;j<len;j++)
        {
            if(intervals[j].start<= ans.back().End)
            {
                if(intervals[j].End<= ans.back().End) continue;
                else
                   ans.back().End = intervals[j].End;
            }
            else
            {
                ans.push_back(intervals[j]);
            }
        }
        return ans;
    }
private:
    bool cmp(struct Interval x,struct Interval y){
        if(x.start == y.start)
            return x.End<y.End;
        else
            return x.start<y.start;
    }
};

int main()
{
    int n,x,y;
    vector<Interval> interval;
    Interval tmp;
    Solution S;
    while(cin>>n)
    {
        interval.clear();
        for(int i=0;i<n;i++)
        {
            cin>>tmp.start>>tmp.End;
            interval.push_back(tmp);
        }
        interval = S.merge(interval);
        for(int j=0;j<interval.size();j++)
            cout<<interval[j].start<<" "<<interval[j].End<<endl;
    }
    return 0;
}
