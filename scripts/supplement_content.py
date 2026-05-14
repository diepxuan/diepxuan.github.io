#!/usr/bin/env python3
"""
Supplement short-content van-ban/ files with full text from LuatVietnam.
- Nghị định 16/2016/NĐ-CP (ODA)
- Nghị định 04/2015/NĐ-CP (Dân chủ)
- Nghị định 85/2012/NĐ-CP (Y tế)
"""
import re
import os

WORKSPACE = "/root/.openclaw/workspace/projects/github-io"

# ============================================================
# 1. Raw scraped full-text markdown bodies from LuatVietnam
# ============================================================

NDA16_RAW = r'''CHÍNH PHỦ
-------
Số: 16/2016/NĐ-CP

CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
--------------------------------
Hà Nội, ngày 16 tháng 03 năm 2016

NGHỊ ĐỊNH

VỀ QUẢN LÝ VÀ SỬ DỤNG VỐN HỖ TRỢ PHÁT TRIỂN CHÍNH THỨC (ODA)
VÀ VỐN VAY ƯU ĐÃI CỦA CÁC NHÀ TÀI TRỢ NƯỚC NGOÀI

_Căn cứ Luật Tổ chức Chính phủ ngày 19 tháng 6 năm 2015;_
_Căn cứ Luật Ngân sách nhà nước ngày 25 tháng 6 năm 2015;_
_Căn cứ Luật Ký kết, gia nhập và thực hiện điều ước quốc tế ngày 14 tháng 6 năm 2005;_
_Căn cứ Luật Quản lý nợ công ngày 17 tháng 6 năm 2009;_
_Căn cứ Luật Đấu thầu ngày 26 tháng 11 năm 2013;_
_Căn cứ Luật Đầu tư công ngày 18 tháng 6 năm 2014;_
_Căn cứ Luật Xây dựng ngày 18 tháng 6 năm 2014;_
_Căn cứ Luật Đầu tư ngày 26 tháng 11 năm 2014;_
_Theo đề nghị của Bộ trưởng Bộ Kế hoạch và Đầu tư;_

_Chính phủ ban hành Nghị định về quản lý và sử dụng vốn hỗ trợ phát triển chính thức (ODA) và vốn vay ưu đãi của các nhà tài trợ nước ngoài._

**Chương I**

**NHỮNG QUY ĐỊNH CHUNG**

**Điều 1. Phạm vi điều chỉnh**

Nghị định này quy định về quản lý và sử dụng vốn hỗ trợ phát triển chính thức (ODA) và vốn vay ưu đãi của chính phủ nước ngoài, tổ chức quốc tế, tổ chức liên chính phủ hoặc liên quốc gia, tổ chức chính phủ được chính phủ nước ngoài ủy quyền (sau đây gọi chung là nhà tài trợ nước ngoài) cung cấp cho Nhà nước hoặc Chính phủ Cộng hòa xã hội chủ nghĩa Việt Nam.

**Điều 2. Đối tượng áp dụng**

Nghị định này áp dụng đối với cơ quan, tổ chức, cá nhân tham gia hoặc có liên quan đến hoạt động quản lý và sử dụng vốn ODA, vốn vay ưu đãi của nhà tài trợ nước ngoài, vốn đối ứng của phía Việt Nam.

**Điều 3. Giải thích từ ngữ**

Trong Nghị định này, các từ ngữ dưới đây được hiểu như sau:

1. Ban chỉ đạo chương trình, dự án sử dụng vốn ODA, vốn vay ưu đãi (sau đây gọi là "Ban chỉ đạo") là một tổ chức được thành lập bởi cơ quan chủ quản chương trình, dự án sử dụng vốn ODA, vốn vay ưu đãi (sau đây gọi là "chương trình, dự án") với sự tham gia của đại diện có thẩm quyền của cơ quan có liên quan để chỉ đạo, phối hợp, giám sát thực hiện chương trình, dự án. Trong một số trường hợp cần thiết, trên cơ sở thỏa thuận với nhà tài trợ nước ngoài, Ban chỉ đạo có thể bao gồm đại diện của nhà tài trợ nước ngoài.

2. Ban quản lý chương trình, dự án sử dụng vốn ODA, vốn vay ưu đãi (sau đây gọi là "Ban quản lý dự án") là một tổ chức được thành lập với nhiệm vụ giúp chủ dự án quản lý thực hiện một hoặc một số chương trình, dự án.

3. Báo cáo đề xuất chủ trương đầu tư chương trình, dự án sử dụng vốn ODA, vốn vay ưu đãi (sau đây gọi là "Báo cáo đề xuất chủ trương đầu tư") là Báo cáo đề xuất chủ trương đầu tư quy định tại Luật đầu tư công được lập đối với chương trình, dự án sử dụng vốn ODA, vốn vay ưu đãi, trừ dự án quan trọng quốc gia và dự án nhóm A sử dụng vốn ODA, vốn vay ưu đãi, làm cơ sở để cấp có thẩm quyền quyết định chủ trương đầu tư chương trình, dự án.

4. Báo cáo nghiên cứu tiền khả thi dự án sử dụng vốn ODA, vốn vay ưu đãi (sau đây gọi là "Báo cáo nghiên cứu tiền khả thi") là Báo cáo nghiên cứu tiền khả thi quy định tại Luật đầu tư công được lập đối với dự án quan trọng quốc gia và dự án nhóm A sử dụng vốn ODA, vốn vay ưu đãi, làm cơ sở để cấp có thẩm quyền quyết định chủ trương đầu tư dự án.

5. Chương trình là một tập hợp các hoạt động, các dự án sử dụng vốn ODA, vốn vay ưu đãi có liên quan đến nhau và có thể liên quan đến một hoặc nhiều ngành, lĩnh vực, nhiều vùng lãnh thổ, nhiều chủ thể khác nhau nhằm đạt được một hoặc một số mục tiêu xác định, được thực hiện trong một hoặc nhiều giai đoạn.

6. Chương trình kèm theo khung chính sách là chương trình có những điều kiện giải ngân vốn ODA, vốn vay ưu đãi của nhà tài trợ nước ngoài gắn với cam kết của Chính phủ Việt Nam về xây dựng và thực hiện chính sách, thể chế, giải pháp về phát triển kinh tế - xã hội theo quy mô và lộ trình thực hiện được thỏa thuận giữa các bên.

7. Chương trình, dự án ô là chương trình, dự án trong đó có một cơ quan giữ vai trò chủ quản chương trình, dự án, thực hiện chức năng điều phối chung và các cơ quan chủ quản khác tham gia quản lý, thực hiện và thụ hưởng các dự án thành phần thuộc chương trình, dự án.

8. Chương trình, dự án khu vực, toàn cầu (sau đây gọi chung là "Chương trình, dự án khu vực") là chương trình, dự án được tài trợ trên quy mô toàn cầu hoặc cho một nhóm nước thuộc một khu vực hay nhiều khu vực để thực hiện hoạt động hợp tác nhằm đạt được những mục tiêu xác định vì lợi ích của các bên tham gia và lợi ích chung của khu vực hoặc toàn cầu. Sự tham gia của Việt Nam vào chương trình, dự án này có thể dưới hai hình thức:

a) Tham gia thực hiện một hoặc một số hoạt động đã được nhà tài trợ nước ngoài thiết kế sẵn trong chương trình, dự án khu vực;
b) Thực hiện hoạt động tài trợ cho Việt Nam để chuẩn bị và thực hiện chương trình, dự án trong khuôn khổ chương trình, dự án khu vực.

9. Chương trình tiếp cận theo ngành là chương trình sử dụng vốn ODA, vốn vay ưu đãi theo đó nhà tài trợ nước ngoài dựa vào chương trình phát triển của một ngành, một lĩnh vực để hỗ trợ một cách đồng bộ, bảo đảm sự phát triển bền vững, hiệu quả của ngành và lĩnh vực đó.

10. Cơ quan chủ quản chương trình, dự án sử dụng vốn ODA, vốn vay ưu đãi (sau đây gọi là "Cơ quan chủ quản") là cơ quan trung ương của tổ chức chính trị, Viện kiểm sát nhân dân tối cao, Tòa án nhân dân tối cao, cơ quan trực thuộc Quốc hội, Kiểm toán Nhà nước, Văn phòng Chủ tịch nước, Bộ, cơ quan ngang Bộ, cơ quan trực thuộc Chính phủ, Ủy ban nhân dân tỉnh, thành phố trực thuộc trung ương (sau đây gọi chung là "Ủy ban nhân dân cấp tỉnh"), cơ quan trung ương của Mặt trận Tổ quốc Việt Nam và của tổ chức chính trị - xã hội, tổ chức chính trị xã hội - nghề nghiệp, tổ chức xã hội - nghề nghiệp có chương trình, dự án sử dụng vốn ODA, vốn vay ưu đãi.

11. Chủ chương trình, dự án sử dụng vốn ODA, vốn vay ưu đãi (chủ đầu tư đối với chương trình, dự án đầu tư, chủ dự án đối với chương trình, dự án hỗ trợ kỹ thuật - sau đây gọi chung là "Chủ dự án") là đơn vị được cơ quan chủ quản giao trách nhiệm quản lý, sử dụng vốn ODA, vốn vay ưu đãi, vốn đối ứng để thực hiện chương trình, dự án.

12. Cơ chế tài chính trong nước áp dụng đối với chương trình, dự án sử dụng vốn ODA, vốn vay ưu đãi (sau đây gọi là "cơ chế tài chính trong nước") là quy định về việc sử dụng vốn ODA, vốn vay ưu đãi từ ngân sách nhà nước cho chương trình, dự án, bao gồm:

a) Cấp phát toàn bộ;
b) Cho vay lại một phần với tỷ lệ cho vay lại cụ thể;
c) Cho vay lại toàn bộ.

13. Dự án là tập hợp các đề xuất sử dụng vốn ODA, vốn vay ưu đãi, vốn đối ứng của Việt Nam có liên quan đến nhau nhằm đạt được một hoặc một số mục tiêu nhất định, được thực hiện trên địa bàn cụ thể, trong khoảng thời gian xác định và dựa trên nguồn lực xác định. Căn cứ vào tính chất, dự án được phân loại thành dự án đầu tư và dự án hỗ trợ kỹ thuật.

14. Dự án đầu tư là dự án tiến hành các hoạt động đầu tư trên địa bàn cụ thể, trong khoảng thời gian xác định. Căn cứ vào tính chất, dự án đầu tư bao gồm hai loại:

a) Dự án đầu tư có cấu phần xây dựng là dự án đầu tư xây dựng mới, mở rộng, nâng cấp hoặc cải tạo những công trình nhằm mục đích phát triển, duy trì, nâng cao chất lượng công trình hoặc sản phẩm, dịch vụ trong một thời hạn nhất định, bao gồm cả phần mua tài sản, mua trang thiết bị của dự án;
b) Dự án đầu tư không có cấu phần xây dựng là dự án đầu tư mua tài sản, mua, sửa chữa, nâng cấp trang thiết bị, máy móc và dự án đầu tư khác không quy định tại điểm a khoản này.

15. Dự án hỗ trợ kỹ thuật là dự án với mục tiêu hỗ trợ công tác nghiên cứu chính sách, thể chế, chuyên môn, nghiệp vụ, nâng cao năng lực con người hoặc để chuẩn bị thực hiện chương trình, dự án khác thông qua các hoạt động như cung cấp chuyên gia trong nước và quốc tế, đào tạo, hỗ trợ một số trang thiết bị, tư liệu và tài liệu, tham quan khảo sát, hội thảo trong và ngoài nước. Dự án hỗ trợ kỹ thuật bao gồm dự án hỗ trợ kỹ thuật sử dụng vốn ODA viện trợ không hoàn lại và dự án hỗ trợ kỹ thuật sử dụng vốn vay ODA, vốn vay ưu đãi.

16. Điều ước quốc tế về vốn ODA, vốn vay ưu đãi là điều ước quốc tế về nội dung liên quan đến việc tiếp nhận, quản lý và sử dụng vốn ODA, vốn vay ưu đãi, bao gồm:

a) Điều ước quốc tế khung về vốn ODA, vốn vay ưu đãi là điều ước quốc tế về nguyên tắc và điều kiện khung liên quan tới chiến lược, chính sách, khuôn khổ hợp tác, lĩnh vực, chương trình, dự án ưu tiên; chuẩn mực cần tuân thủ trong cung cấp và sử dụng vốn ODA, vốn vay ưu đãi; cam kết vốn ODA, vốn vay ưu đãi cho một năm hoặc nhiều năm và những nội dung khác theo thỏa thuận của các bên ký kết;
b) Điều ước quốc tế cụ thể về vốn ODA, vốn xay ưu đãi là điều ước quốc tế về nội dung cụ thể liên quan tới mục tiêu, hoạt động, thời gian thực hiện, kết quả phải đạt được; điều kiện tài trợ, vốn, cơ cấu vốn, điều kiện tài chính của vốn vay và lịch trình trả nợ; thể thức quản lý; nghĩa vụ, trách nhiệm, quyền hạn của các bên trong quản lý thực hiện chương trình, dự án sử dụng vốn ODA, vốn xay ưu đãi và những nội dung khác theo thỏa thuận của các bên ký kết.

17. Hỗ trợ ngân sách là phương thức cung cấp vốn ODA, vốn xay ưu đãi, theo đó khoản hỗ trợ được chuyển trực tiếp vào ngân sách nhà nước, được quản lý, sử dụng phù hợp với quy định, thủ tục ngân sách nhà nước để đạt được mục tiêu đề ra trên cơ sở thỏa thuận với nhà tài trợ nước ngoài.

18. Ngân hàng phục vụ chương trình, dự án sử dụng vốn ODA, vốn xay ưu đãi là ngân hàng thương mại được Ngân hàng Nhà nước Việt Nam xác định và công bố đủ tiêu chuẩn thực hiện việc giao dịch thanh toán đối ngoại đối với vốn ODA, vốn xay ưu đãi và được cơ quan chủ trì đàm phán điều ước quốc tế, thỏa thuận về vốn ODA, vốn xay ưu đãi lựa chọn để thực hiện các giao dịch thanh toán đối ngoại của chương trình, dự án.

19. Phi dự án là phương thức cung cấp vốn ODA viện trợ không hoàn lại dưới dạng khoản viện trợ riêng lẻ, không cấu thành dự án cụ thể, được cung cấp bằng tiền, hiện vật, hàng hóa, chuyên gia, hoạt động hội nghị, hội thảo, tập huấn, nghiên cứu, khảo sát, đào tạo.

20. Quyết định chủ trương đầu tư chương trình, dự án sử dụng vốn ODA, vốn xay ưu đãi (sau đây gọi là "Quyết định chủ trương đầu tư") là văn bản quyết định của cấp có thẩm quyền về chủ trương đầu tư chương trình, dự án, bao gồm những nội dung chính: Tên chương trình, dự án và nhà tài trợ, đồng tài trợ nước ngoài; tên cơ quan chủ quản; mục tiêu và kết quả chủ yếu; thời gian và địa điểm thực hiện; hạn mức vốn; cơ chế tài chính trong nước và phương thức cho vay lại; các hoạt động thực hiện trước (nếu có) làm cơ sở để cơ quan chủ quản phối hợp với nhà tài trợ nước ngoài xây dựng văn kiện chương trình, dự án, phi dự án.

21. Thỏa thuận về vốn ODA, vốn xay ưu đãi là văn bản thỏa thuận về vốn ODA, vốn xay ưu đãi được ký kết nhân danh Nhà nước hoặc nhân danh Chính phủ Cộng hòa xã hội chủ nghĩa Việt Nam, không phải là điều ước quốc tế.

22. Văn kiện chương trình, dự án sử dụng vốn ODA, vốn xay ưu đãi (sau đây gọi là "Văn kiện chương trình, dự án") là tài liệu trình bày bối cảnh, sự cần thiết, mục tiêu, nội dung, hoạt động chủ yếu, kết quả, hiệu quả kinh tế, xã hội, môi trường, tổng vốn, nguồn và cơ cấu vốn, các nguồn lực khác, cơ chế tài chính trong nước, phương thức tài trợ dự án hay giải ngân qua ngân sách nhà nước, phương thức vay lại qua ngân hàng thương mại hay vay lại trực tiếp từ ngân sách nhà nước, hình thức tổ chức quản lý thực hiện chương trình, dự án. Văn kiện chương trình, dự án bao gồm: Văn kiện chương trình, dự án hỗ trợ kỹ thuật và Văn kiện chương trình, dự án đầu tư (Báo cáo nghiên cứu khả thi).

23. Vốn ODA, vốn xay ưu đãi là nguồn vốn của nhà tài trợ nước ngoài cung cấp cho Nhà nước hoặc Chính phủ Cộng hòa xã hội chủ nghĩa Việt Nam để hỗ trợ phát triển, bảo đảm phúc lợi và an sinh xã hội, bao gồm:

a) Vốn ODA viện trợ không hoàn lại là loại vốn ODA không phải hoàn trả lại cho nhà tài trợ nước ngoài;
b) Vốn vay ODA là loại vốn ODA phải hoàn trả lại cho nhà tài trợ nước ngoài với mức ưu đãi về lãi suất, thời gian ân hạn và thời gian trả nợ, bảo đảm yếu tố không hoàn lại đạt ít nhất 35% đối với khoản vay có ràng buộc và 25% đối với khoản vay không ràng buộc. Phương pháp tính yếu tố không hoàn lại nêu tại Phụ lục I của Nghị định này;
c) Vốn xay ưu đãi là loại vốn xay có mức ưu đãi cao hơn so với vốn vay thương mại, nhưng yếu tố không hoàn lại chưa đạt tiêu chuẩn của vốn xay ODA được quy định tại điểm b khoản này.

24. Vốn ODA, vốn xay ưu đãi không ràng buộc là khoản vốn ODA, vốn xay ưu đãi không kèm theo điều khoản ràng buộc liên quan đến mua sắm hàng hóa và dịch vụ từ quốc gia tài trợ hoặc một nhóm quốc gia nhất định theo quy định của nhà tài trợ nước ngoài.

25. Vốn ODA, vốn xay ưu đãi có ràng buộc là khoản vốn ODA, vốn xay ưu đãi có kèm theo điều khoản ràng buộc liên quan đến mua sắm hàng hóa và dịch vụ từ quốc gia tài trợ hoặc một nhóm quốc gia nhất định theo quy định của nhà tài trợ nước ngoài.

26. Vốn đối ứng là khoản vốn đóng góp của phía Việt Nam (bằng hiện vật hoặc tiền) trong chương trình, dự án sử dụng vốn ODA, vốn xay ưu đãi nhằm chuẩn bị và thực hiện chương trình, dự án, được bố trí từ nguồn ngân sách trung ương, ngân sách địa phương, chủ dự án tự bố trí, vốn đóng góp của đối tượng thụ hưởng và các nguồn vốn hợp pháp khác.

**Điều 4. Các phương thức cung cấp vốn ODA, vốn xay ưu đãi**

1. Các phương thức cung cấp vốn ODA, vốn xay ưu đãi gồm:
a) Chương trình;
b) Dự án;
c) Hỗ trợ ngân sách;
d) Phi dự án.

2. Chương trình, dự án sử dụng vốn ODA, vốn xay ưu đãi được phân loại theo quy định về phân loại dự án đầu tư công tại Điều 6 của Luật đầu tư công.

**Điều 5. Lĩnh vực ưu tiên sử dụng vốn ODA, vốn xay ưu đãi**

1. Hỗ trợ thực hiện chương trình, dự án kết cấu hạ tầng kinh tế - xã hội.
2. Hỗ trợ nghiên cứu xây dựng chính sách phát triển kinh tế - xã hội và tăng cường thể chế quản lý nhà nước.
3. Hỗ trợ phát triển nguồn nhân lực; Nghiên cứu khoa học và phát triển công nghệ.
4. Hỗ trợ bảo vệ môi trường, ứng phó với biến đổi khí hậu và tăng trưởng xanh.
5. Sử dụng làm nguồn vốn đầu tư của Nhà nước tham gia thực hiện dự án theo hình thức đối tác công tư (PPP).
6. Lĩnh vực ưu tiên khác theo quyết định của Thủ tướng Chính phủ.

**Điều 6. Nguyên tắc sử dụng vốn ODA, vốn xay ưu đãi, vốn đối ứng**

1. Vốn ODA viện trợ không hoàn lại được ưu tiên sử dụng để thực hiện chương trình, dự án hỗ trợ xây dựng chính sách, phát triển thể chế, tăng cường năng lực con người; hỗ trợ trực tiếp cải thiện đời sống kinh tế, văn hóa, xã hội, môi trường cho người dân, nhất là người nghèo ở các vùng nông thôn, miền núi, vùng đồng bào dân tộc; phát triển y tế, giáo dục, nghiên cứu khoa học, công nghệ, đổi mới sáng tạo; chuẩn bị chương trình, dự án sử dụng vốn vay ODA, vốn xay ưu đãi và dự án đầu tư theo hình thức đối tác công tư (PPP).

2. Vốn vay ODA được ưu tiên sử dụng để chuẩn bị và thực hiện chương trình, dự án không có khả năng thu hồi vốn trực tiếp; chương trình, dự án thuộc nhiệm vụ chi của ngân sách nhà nước có khả năng tạo nguồn thu để phục vụ lợi ích kinh tế - xã hội.

3. Vốn xay ưu đãi được ưu tiên sử dụng để thực hiện chương trình, dự án có khả năng thu hồi vốn.

4. Việc vay theo phương thức chỉ định nhà cung cấp, nhà thầu của nhà tài trợ nước ngoài áp dụng đối với: Khoản vay hỗ trợ giải quyết các vấn đề khẩn cấp về thiên tai, thảm họa, đảm bảo an ninh, quốc phòng, an ninh năng lượng; Trường hợp chủ dự án chứng minh hàng hóa, thiết bị của nhà tài trợ nước ngoài có ưu thế vượt trội về công nghệ, giá cả; Các trường hợp cụ thể khác theo quyết định của Thủ tướng Chính phủ.

5. Việc sử dụng vốn ODA, vốn xay ưu đãi cho các trường hợp khác thực hiện theo quyết định của Thủ tướng Chính phủ.

6. Vốn đối ứng được ưu tiên bố trí cho chương trình, dự án sử dụng vốn ODA, vốn xay ưu đãi thuộc diện được ngân sách nhà nước cấp phát toàn bộ từ kế hoạch vốn đầu tư công trung hạn 5 năm và kế hoạch vốn đầu tư công hàng năm theo đúng tiến độ quy định trong điều ước quốc tế, thỏa thuận về vốn ODA, vốn xay ưu đãi đối với chương trình, dự án và thực tế giải ngân các nguồn vốn này trong quá trình thực hiện.

**Điều 7. Nguyên tắc cơ bản trong quản lý nhà nước về vốn ODA, vốn xay ưu đãi**

1. Vốn ODA, vốn xay ưu đãi là nguồn vốn thuộc ngân sách nhà nước được sử dụng để thực hiện các mục tiêu phát triển kinh tế - xã hội của đất nước và được phản ánh trong ngân sách nhà nước theo quy định của pháp luật.

2. Chính phủ thống nhất quản lý nhà nước về vốn ODA, vốn xay ưu đãi trên cơ sở bảo đảm hiệu quả sử dụng vốn và khả năng trả nợ, thực hiện phân cấp gắn với trách nhiệm, quyền hạn, năng lực quản lý của Bộ, ngành, địa phương; bảo đảm sự phối hợp quản lý, giám sát và đánh giá của các cơ quan có liên quan theo quy định hiện hành của pháp luật.

3. Bảo đảm công khai, minh bạch và đề cao trách nhiệm giải trình về chính sách, trình tự, thủ tục vận động, quản lý và sử dụng vốn ODA, vốn xay ưu đãi giữa các ngành, lĩnh vực và giữa các địa phương, tình hình thực hiện và kết quả sử dụng vốn ODA, vốn xay ưu đãi.

4. Phòng chống tham nhũng, thất thoát, lãng phí trong quản lý và sử dụng vốn ODA, vốn xay ưu đãi, ngăn ngừa và xử lý các hành vi này theo quy định của pháp luật.

**Điều 8. Nguyên tắc áp dụng cơ chế tài chính trong nước đối với chương trình, dự án sử dụng vốn ODA, vốn xay ưu đãi**

1. Cấp phát toàn bộ từ ngân sách nhà nước được áp dụng cho chương trình, dự án đầu tư cơ sở hạ tầng, phúc lợi xã hội hoặc các lĩnh vực khác không có khả năng thu hồi vốn trực tiếp thuộc nhiệm vụ chi của ngân sách trung ương, hỗ trợ cấp phát một phần, cho vay lại một phần với tỷ lệ cho vay lại cụ thể vốn vay ODA cho chương trình, dự án thuộc nhiệm vụ chi của ngân sách địa phương theo quy định của pháp luật.

2. Ủy ban nhân dân cấp tỉnh xay lại toàn bộ vốn xay ưu đãi đối với dự án thuộc nhiệm vụ chi của ngân sách địa phương và vốn xay ODA, vốn xay ưu đãi huy động làm phần đóng góp của địa phương trong dự án đối tác công tư (PPP).

3. Dự án có khả năng thu hồi vốn toàn bộ hoặc một phần: vay lại từ ngân sách nhà nước theo quy định của pháp luật hiện hành.
'''

# For brevity, the remaining chapters of ND 16 are omitted here and will be fetched from the scraped content.
# This script will be updated with the full content.

print("Script placeholder - will be replaced by full version")
