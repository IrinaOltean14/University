package model.ADT;

import model.exception.ADTException;

import java.util.Map;
public interface IFileTable<K, V> {
    public V lookup(K key);
    public void update(K key, V value);
    public void remove(K key);
    boolean isDefined(K key);
    void add(K key, V value) throws ADTException;
    public Map<K, V> getContent();
}
