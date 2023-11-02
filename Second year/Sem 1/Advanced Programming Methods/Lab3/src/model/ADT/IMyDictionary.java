package model.ADT;

import model.exception.ADTException;
import model.exception.MyException;

public interface IMyDictionary<K, V> {
    void add(K key, V value) throws ADTException;
    boolean isDefined(K key);
    public V lookup(K key);

    public void update(K key, V value);
}
