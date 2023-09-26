movies_list = ("conan" , "goku" , "sieu nhan gao" , "cappppp" , "gió" ,)
movies_list = list(movies_list)

# tạo movies list chứa tên các bộ phim đã xem 
print ( "phim đã xem: ", movies_list)

#2 sử dụng hàm input để nhập vào một bộ phim khác không óc trong movies list
moives_list_new = input ("mời bạn nhập tên phim : ")

#3 thêm bộ phim vừa nhập vào cuối danh sách
movies_list.append (moives_list_new)
print("phim đã xem :", movies_list)
#4 in ra bộ phim đầu tiên , cuối cùng và ở giữa movies list
print(f"bộ phim đầu tiên trong danh sách là :  {movies_list[0]}")
print(f"bộ phim cuối cùng trong danh sách là :  {movies_list[-1]}")
amount = len(movies_list)
print(f"bộ phim ở giữa trong danh sách là :  {movies_list[amount // 2]}")

#5 tính tổng sóo bộ phim đã xem 
amount = len(movies_list)
print(f"tổng bộ phim đã xem là : " , amount)
#6 xóa bộ phim đầu và cuối 
first_value_in_movies_list = movies_list
last_value_in_movies_list = movies_list.pop()
print("tên bộ phim cuối cùng trong danh sách là : " , last_value_in_movies_list)
print("danh sách sau khi xóa là : " , movies_list)

#7 lấy ra và xóa bộ phim cuối cùng trong movies list 
print("bộ phim cuối cungf là : " ,last_value_in_movies_list)
print("danh sách sau khi xóa bộ phim cuối cùng là : " ,movies_list)

#8 chèn một bộ phim bất kì vào đàu danh sách movies
movies_list.insert (0,"bạch tuyết và bảy chú lùn ")
print("danh sách bộ phim mới cập nhật " , movies_list )

#9 đếm số bộ phim có tiên đề là " Pne Piece"
amount = movies_list.count("One Piece")
print("bộ phim có tiêu đề one piece đang có : ", amount)

#10 tìm vị trí cảu bộ phim cso tên là " gió"
index_of_gio = movies_list.index('gió')
print (" vị trí cảu gió là : " , index_of_gio)

#11 thêm một danh sách bộ phim có trong danh sách
movies_list.append("lập trình python")
print("danh sách phim có hiện tại là : " , movies_list)

#12 xóa tất cả các bộ phim có trong danh sách
movies_list.clear()
print("danh sách phim hiện có" , movies_list)