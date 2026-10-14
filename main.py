#DataFrame
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data={"Họ và tên": ["Nguyễn Văn An","Trần Thị Bình", "Nguyễn Đức Trí", "Phạm Hoài Giang", "Ngô Minh Đức", 
                    "Đỗ Đức Long", "Nguyễn Thị Yến","Bùi Ngọc Khánh", "Đỗ Duy Quang", "Vũ Ngọc Thương" ],
      "Chuyên cần": [9, 8, 6, 6, 7, 9, 8, 8, 9, 7],
      "Giữa kỳ": [8, 7, 8, 7, 8, 9, 10, 8, 10, 6],
      "Cuối kỳ": [9, 6, 9, 8, 9, 10, 10, 8, 9, 8],
      "Tên": ["An", "Bình","Trí", "Giang", "Đức", "Long", "Yến", "Khánh", "Quang", "Thương" ]}
df = pd.DataFrame(data)
df.index=range(1, len(df)+1)
print("BẢNG ĐIỂM:")
print(df.to_string(index=False))

#Điểm tổng kết
df["Tổng kết"]=(0.2*df["Chuyên cần"]+0.3*df["Giữa kỳ"]+0.5*df["Cuối kỳ"])
df["Tổng kết"]=df["Tổng kết"].round(2)
print("BẢNG ĐIỂM TỔNG KẾT:")
print(df.to_string(index=False))

#Xếp loại
df["Xếp loại"]=df["Tổng kết"].apply(lambda diem: "Giỏi" if diem>=8.5
                                         else "Khá" if diem>=7.0
                                         else "Trung bình" if diem >=5.0
                                         else "Yếu")
print(df)

#Thống kê
#1. điêm trung bình
diem_trung_binh=df["Tổng kết"].mean()
print("Điểm tổng kết trung bình của lớp:", round(diem_trung_binh, 2))

#2. điểm cao nhất
diem_cao_nhat=df["Tổng kết"].max()
sinh_vien_cao_nhat=df[df["Tổng kết"]==diem_cao_nhat]
print("\nSinh viên có điểm tổng kết cao nhất:")
print(sinh_vien_cao_nhat)

#3. điểm thấp nhất
diem_thap_nhat=df["Tổng kết"].min()
sinh_vien_thap_nhat=df[df["Tổng kết"]==diem_thap_nhat]
print("\nSinh viên có điểm tổng kết thấp nhất:")
print(sinh_vien_thap_nhat)

#Điểm >=5
so_sinh_vien_dat=(df["Tổng kết"]>=5).sum()
print("\nSố sinh viên đạt:", so_sinh_vien_dat)

#Trực quan hóa
fig, ax = plt.subplots(figsize=(12, 5))
bars=ax.bar(df["Tên"], df["Tổng kết"], color="cornflowerblue")
ax.set_title("Điểm tổng kết của sinh viên")
ax.set_xlabel("Tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.show()

#Tạo web bằng streamlit
#Tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.markdown("---")
#Hiển thị bảng điểm 
st.subheader("1. Bảng điểm của sinh viên")
cot_hien_thi=["Họ và tên", "Chuyên cần", "Giữa Kỳ", "Cuối kỳ", "Tổng kết", "Xếp loại"]
st.dataframe(df[cot_hien_thi], use_container_width=True, hide_index=True)
#Thống kê điểm
st.subheader("2. Thống kê kết quả học tập")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Điểm trung bình của lớp", f"{diem_trung_binh:.2f}")
col2.metric("Điểm cao nhất", f"{diem_cao_nhat:.2f}")
col3.metric("Điểm thấp nhất", f"{diem_thap_nhat:.2f}")
col4.metric("Số sinh viên đạt", f"{so_sinh_vien_dat:.2f}")
st.write("**Sinh viên có điểm tổng kết cao nhất:**")
st.dataframe(sinh_vien_cao_nhat[cot_hien_thi], use_container_width=True, hide_index=True)
st.write("**Sinh viên có điểm tổng kết thấp nhất:**")
st.dataframe(sinh_vien_thap_nhat[cot_hien_thi], use_container_width=True, hide_index=True)
#Danh sách chọn
st.subheader("3. Tra cứu thông tin sinh viên")
danh_sach=df["Họ và tên"].tolist()
ten_duoc_chon=st.selectbox("Chọn một sinh viên:", danh_sach)
sinh_vien=df[df["Họ và tên"]==ten_duoc_chon].iloc[0]
st.write("**Thông tin chi tiết sinh viên được chọn:**")
col1, col2 = st.columns(2)
with col1:
    st.write(f"**Họ và tên:**{sinh_vien['Họ và tên']}")
    st.write(f"**Chuyên cần:**{sinh_vien['Chuyên cần']:.2f}")
with col2:
    st.write(f"**Giữa kỳ:**{sinh_vien['Giữa kỳ']:.2f}")
    st.write(f"**Cuối kỳ:**{sinh_vien['Cuối kỳ']:.2f}")
    st.write(f"**Tổng kết:**{sinh_vien['Tổng kết']:.2f}")
    st.write(f"**Xếp loại:**{sinh_vien['Xếp loại']}")
#Biểu đồ cột điểm tổng kết
st.subheader("4. Biểu đồ điểm tổng kết của sinh viên")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.subplots.bar_label(bars, fmt="%.2f", padding=3)
st.pyplot(fig)
plt.close(fig)
#Hiển thị thông tin người tạo
st.markdown("---")
st.caption("Người tạo ứng dụng: [Võ Tuấn Kiệt] | MSSV: [058208003139]")
st.caption("Ứng dụng quản lý điểm sinh viên bằng")