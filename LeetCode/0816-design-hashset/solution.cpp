class MyHashSet {
public:
  vector<int> val;
    MyHashSet() {
     vector<int> val; 
    }
    
    void add(int key) {
        val.push_back(key);
    }
    
    void remove(int key) {
        for (int i = 0; i < val.size(); i++) {
          if (val[i] == key) {
            val.erase(val.begin() + i);
          }
        }
    }
    
    bool contains(int key) {
        if (std::find(val.begin(), val.end(), key) != val.end()) {
          return true;
        }
        else {return false;}
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
