package model.ADT;

import model.exception.ADTException;

import java.util.Map;

public interface IMyDictionary<K, V> {
    void add(K key, V value) throws ADTException;
    boolean isDefined(K key);
    public V lookup(K key);

    public void update(K key, V value);

    Map<K,V> getContent();

    IMyDictionary<K,V> deepCopy() throws ADTException;
}
