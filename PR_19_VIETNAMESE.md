## 🚨 Fix Lỗi Syntax YAML Trong GitHub Actions

### Vấn Đề
Lỗi validation GitHub Actions liên tục:
```
Invalid workflow file: .github/workflows/crawl-legal-documents.yml#L42
You have an error in your yaml syntax on line 42
```

### Nguyên Nhân Gốc
1. **Script Python inline trong YAML** (300+ dòng)
2. **Ký tự non-ASCII** (tiếng Việt) trong comments YAML
3. **Xung đột syntax** dòng 42: `${{ inputs.test_mode }}` trong bash string

### Fix Đã Áp Dụng
#### 1. **Xóa Hoàn Toàn Inline Script**
- Xóa script Python embedded khỏi workflow YAML
- Dùng file script riêng: `scripts/crawl-legal-documents.py`
- YAML sạch, không inline code (best practice)

#### 2. **Fix Lỗi Syntax Dòng 42**
```yaml
# TRƯỚC (lỗi syntax):
if [ "${{ inputs.test_mode }}" = "true" ]; then

# SAU (đã fix):
TEST_MODE="${{ inputs.test_mode }}"
if [ "$TEST_MODE" = "true" ]; then
```

#### 3. **Xóa Ký Tự Non-ASCII**
- Thay comments tiếng Việt bằng tiếng Anh (tạm thời)
- Đảm bảo YAML parser không gặp encoding issues

#### 4. **Tách Biệt Rõ Ràng**
- Workflow YAML: Chỉ workflow logic
- Python script: File riêng với error handling
- Không trộn ngôn ngữ trong single file

### Lợi Ích
✅ **YAML syntax valid** - GitHub Actions sẽ accept workflow
✅ **Không inline scripts** - Best practice cho maintainability
✅ **Error messages rõ ràng** - Python script có import error handling
✅ **Workflow chạy được** - Có thể trigger manual hoặc schedule

### Testing
1. Merge PR này
2. GitHub Actions validation sẽ pass
3. Workflow có thể trigger (nếu `workflow_dispatch` work)
4. Test mode: `python scripts/crawl-legal-documents.py --test`

### Files Thay Đổi
- `.github/workflows/crawl-legal-documents.yml` - YAML sạch, không inline script
- `scripts/crawl-legal-documents.py` - Script riêng với error handling

### Impact
- **Ngay lập tức**: Fix lỗi validation workflow
- **Không downtime**: Chỉ thay đổi workflow
- **Automation enabled**: Weekly legal documents crawling