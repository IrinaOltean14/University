package model.ADT;
import java.util.List;
import model.exception.ADTException;

public interface IMyList<T> {
    void add(T item);
    void remove(T item) throws ADTException;

    List<T> getContent();
}
