merge_sort: main merge_sort.js merge_sort.py
	./main
	js merge_sort.js
	../venv/bin/python merge_sort.py

insertion: main insertion_sort.js insertion_sort.py
	./main
	js insertion_sort.js
	../venv/bin/python insertion_sort.py

selection: main selection_sort.js selection_sort.py
	./main
	js selection_sort.js
	../venv/bin/python selection_sort.py

main: sort.o main.o
	g++ -o $@ $^

sort.o: sort.cpp
	g++ -c $^ -o $@

main.o: main.cpp
	g++ -c $^ -o $@

clean:
	rm -rf *.o main