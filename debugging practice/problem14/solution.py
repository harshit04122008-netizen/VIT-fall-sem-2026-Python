def reading_progress(total_pages, pages_read=0):
    pages_remaining = total_pages - pages_read
    completion_percent = (pages_read / total_pages) * 100
    return pages_remaining, completion_percent

total_pages = int(input())
pages_read = int(input())

if pages_read == 0:
    pages_remaining, completion_percent = reading_progress(total_pages)
else:
    pages_remaining, completion_percent = reading_progress(total_pages, pages_read)

print("Pages Remaining:", pages_remaining)
print(f"Completion Percent: {completion_percent:.1f}")