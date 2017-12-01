from decksite.data import deck
from shared import dtutil

# Results that were reported despite opponent having no deck, numbers are deck_id
# 9/1/2016 21:52:17    153    Silmerion    Loss    1-2
# 9/11/2016 10:54:50    200    chrigugigu    Loss    0-2
# 9/11/2016 14:39:30    199    NiekM    Loss    0-2

def disabled():
    # Time is the earliest time that either player reported.
    deck.insert_match(dtutil.parse('8/30/2016 20:13:27', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 141, 2, 140, 0)
    deck.insert_match(dtutil.parse('8/31/2016 1:06:40', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 146, 2, 144, 0)
    deck.insert_match(dtutil.parse('8/31/2016 1:32:28', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 144, 2, 148, 0)
    deck.insert_match(dtutil.parse('8/31/2016 1:55:33', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 150, 2, 151, 0)
    deck.insert_match(dtutil.parse('8/31/2016 1:59:12', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 149, 2, 152, 0)
    deck.insert_match(dtutil.parse('8/31/2016 2:54:28', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 146, 2, 149, 1)
    deck.insert_match(dtutil.parse('8/31/2016 3:26:32', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 153, 2, 150, 1)
    deck.insert_match(dtutil.parse('8/31/2016 6:12:11', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 157, 2, 156, 0)
    deck.insert_match(dtutil.parse('8/31/2016 12:43:09', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 157, 2, 146, 0)
    deck.insert_match(dtutil.parse('8/31/2016 15:14:29', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 146, 2, 147, 1)
    deck.insert_match(dtutil.parse('8/31/2016 15:59:13', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 147, 2, 150, 0)
    deck.insert_match(dtutil.parse('8/31/2016 16:36:03', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 150, 2, 146, 1)
    deck.insert_match(dtutil.parse('8/31/2016 16:46:57', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 147, 2, 144, 0)
    deck.insert_match(dtutil.parse('8/31/2016 17:06:25', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 150, 2, 159, 0)
    deck.insert_match(dtutil.parse('8/31/2016 20:13:20', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 141, 2, 144, 0)
    deck.insert_match(dtutil.parse('8/31/2016 20:40:44', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 160, 2, 155, 1)
    deck.insert_match(dtutil.parse('8/31/2016 22:33:14', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 140, 2, 151, 1)
    deck.insert_match(dtutil.parse('8/31/2016 22:54:14', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 151, 2, 139, 0)
    deck.insert_match(dtutil.parse('8/31/2016 23:13:44', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 144, 2, 139, 0)
    deck.insert_match(dtutil.parse('8/31/2016 23:43:48', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 161, 2, 162, 1)
    deck.insert_match(dtutil.parse('9/1/2016 0:04:23', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 163, 2, 161, 1)
    deck.insert_match(dtutil.parse('9/1/2016 0:07:43', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 162, 2, 151, 1)
    deck.insert_match(dtutil.parse('9/1/2016 0:25:10', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 158, 2, 151, 0)
    deck.insert_match(dtutil.parse('9/1/2016 0:35:27', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 158, 2, 161, 0)
    deck.insert_match(dtutil.parse('9/1/2016 1:09:46', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 164, 2, 161, 1)
    deck.insert_match(dtutil.parse('9/1/2016 1:19:20', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 148, 2, 158, 1)
    deck.insert_match(dtutil.parse('9/1/2016 1:39:18', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 163, 2, 164, 1)
    deck.insert_match(dtutil.parse('9/1/2016 2:39:05', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 164, 2, 153, 1)
    deck.insert_match(dtutil.parse('9/1/2016 13:09:47', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 157, 2, 163, 0)
    deck.insert_match(dtutil.parse('9/1/2016 17:27:16', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 142, 2, 166, 1)
    deck.insert_match(dtutil.parse('9/1/2016 18:29:24', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 166, 2, 162, 0)
    deck.insert_match(dtutil.parse('9/1/2016 20:22:30', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 153, 2, 166, 0)
    deck.insert_match(dtutil.parse('9/2/2016 17:02:22', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 167, 2, 147, 0)
    deck.insert_match(dtutil.parse('9/2/2016 18:30:48', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 168, 2, 147, 0)
    deck.insert_match(dtutil.parse('9/3/2016 2:04:24', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 169, 2, 164, 0)
    deck.insert_match(dtutil.parse('9/3/2016 2:29:14', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 163, 2, 169, 1)
    deck.insert_match(dtutil.parse('9/3/2016 17:27:07', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 171, 2, 166, 1)
    deck.insert_match(dtutil.parse('9/3/2016 17:59:05', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 171, 2, 164, 0)
    deck.insert_match(dtutil.parse('9/3/2016 19:09:12', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 160, 2, 166, 0)
    deck.insert_match(dtutil.parse('9/3/2016 20:33:14', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 160, 2, 169, 1)
    deck.insert_match(dtutil.parse('9/3/2016 22:38:57', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 172, 2, 160, 0)
    deck.insert_match(dtutil.parse('9/3/2016 23:59:06', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 169, 2, 173, 1)
    deck.insert_match(dtutil.parse('9/4/2016 1:12:04', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 172, 2, 169, 0)
    deck.insert_match(dtutil.parse('9/4/2016 1:29:36', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 173, 2, 140, 0)
    deck.insert_match(dtutil.parse('9/4/2016 1:55:01', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 174, 2, 173, 1)
    deck.insert_match(dtutil.parse('9/4/2016 2:05:58', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 163, 2, 140, 0)
    deck.insert_match(dtutil.parse('9/4/2016 12:46:16', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 157, 2, 174, 1)
    deck.insert_match(dtutil.parse('9/4/2016 17:22:49', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 172, 2, 173, 1)
    deck.insert_match(dtutil.parse('9/4/2016 20:06:53', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 174, 2, 172, 1)
    deck.insert_match(dtutil.parse('9/5/2016 2:20:14', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 178, 2, 174, 1)
    deck.insert_match(dtutil.parse('9/5/2016 3:13:32', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 178, 2, 172, 0)
    deck.insert_match(dtutil.parse('9/5/2016 12:18:43', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 157, 2, 167, 1)
    deck.insert_match(dtutil.parse('9/5/2016 13:05:56', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 168, 2, 167, 1)
    deck.insert_match(dtutil.parse('9/6/2016 0:56:16', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 182, 2, 173, 0)
    deck.insert_match(dtutil.parse('9/6/2016 1:24:56', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 174, 2, 182, 0)
    deck.insert_match(dtutil.parse('9/6/2016 1:54:04', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 182, 2, 178, 1)
    deck.insert_match(dtutil.parse('9/6/2016 18:35:04', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 173, 2, 182, 0)
    deck.insert_match(dtutil.parse('9/6/2016 20:27:01', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 167, 2, 182, 0)
    deck.insert_match(dtutil.parse('9/6/2016 20:51:18', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 160, 2, 182, 0)
    deck.insert_match(dtutil.parse('9/6/2016 20:54:20', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 167, 2, 173, 0)
    deck.insert_match(dtutil.parse('9/6/2016 21:24:24', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 170, 2, 161, 1)
    deck.insert_match(dtutil.parse('9/6/2016 21:36:31', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 173, 2, 185, 1)
    deck.insert_match(dtutil.parse('9/6/2016 22:34:24', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 173, 2, 180, 0)
    deck.insert_match(dtutil.parse('9/6/2016 23:00:45', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 184, 2, 186, 0)
    deck.insert_match(dtutil.parse('9/6/2016 23:54:40', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 186, 2, 140, 1)
    deck.insert_match(dtutil.parse('9/7/2016 16:22:45', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 190, 2, 185, 0)
    deck.insert_match(dtutil.parse('9/7/2016 18:06:36', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 185, 2, 189, 0)
    deck.insert_match(dtutil.parse('9/7/2016 20:15:33', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 186, 2, 185, 1)
    deck.insert_match(dtutil.parse('9/7/2016 21:57:38', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 187, 2, 178, 0)
    deck.insert_match(dtutil.parse('9/8/2016 1:55:22', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 184, 2, 188, 1)
    deck.insert_match(dtutil.parse('9/8/2016 21:04:55', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 173, 2, 192, 0)
    deck.insert_match(dtutil.parse('9/8/2016 22:02:57', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 192, 2, 155, 0)
    deck.insert_match(dtutil.parse('9/8/2016 22:24:55', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 194, 2, 193, 1)
    deck.insert_match(dtutil.parse('9/8/2016 22:37:33', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 186, 2, 193, 0)
    deck.insert_match(dtutil.parse('9/8/2016 23:41:50', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 194, 2, 192, 0)
    deck.insert_match(dtutil.parse('9/8/2016 23:58:03', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 192, 2, 184, 1)
    deck.insert_match(dtutil.parse('9/9/2016 0:20:28', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 184, 2, 185, 0)
    deck.insert_match(dtutil.parse('9/9/2016 1:12:04', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 194, 2, 184, 0)
    deck.insert_match(dtutil.parse('9/9/2016 16:50:39', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 190, 2, 193, 0)
    deck.insert_match(dtutil.parse('9/9/2016 22:40:28', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 186, 2, 194, 1)
    deck.insert_match(dtutil.parse('9/9/2016 22:47:49', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 196, 2, 192, 0)
    deck.insert_match(dtutil.parse('9/10/2016 11:39:35', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 207, 2, 198, 1)
    deck.insert_match(dtutil.parse('9/10/2016 12:53:54', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 181, 2, 155, 1)
    deck.insert_match(dtutil.parse('9/10/2016 20:14:30', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 201, 2, 196, 0)
    deck.insert_match(dtutil.parse('9/10/2016 20:49:09', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 202, 2, 170, 0)
    deck.insert_match(dtutil.parse('9/11/2016 7:54:24', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 191, 2, 201, 1)
    deck.insert_match(dtutil.parse('9/11/2016 12:32:42', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 181, 2, 199, 0)
    deck.insert_match(dtutil.parse('9/11/2016 12:45:40', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 190, 2, 201, 1)
    deck.insert_match(dtutil.parse('9/11/2016 13:29:05', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 181, 2, 207, 1)
    deck.insert_match(dtutil.parse('9/11/2016 18:30:42', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 203, 2, 204, 1)
    deck.insert_match(dtutil.parse('9/12/2016 22:23:12', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 196, 2, 207, 0)
    deck.insert_match(dtutil.parse('9/12/2016 23:12:08', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 196, 2, 202, 1)
    deck.insert_match(dtutil.parse('9/13/2016 0:19:39', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 170, 2, 193, 0)
    deck.insert_match(dtutil.parse('9/13/2016 1:23:55', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 204, 2, 193, 1)
    deck.insert_match(dtutil.parse('9/13/2016 17:48:01', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 203, 2, 181, 0)
    deck.insert_match(dtutil.parse('9/13/2016 19:00:03', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 207, 2, 206, 1)
    deck.insert_match(dtutil.parse('9/13/2016 21:15:43', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 207, 2, 187, 1)
    deck.insert_match(dtutil.parse('9/14/2016 17:15:13', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 199, 2, 203, 0)
    deck.insert_match(dtutil.parse('9/15/2016 2:13:18', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 208, 2, 210, 1)
    deck.insert_match(dtutil.parse('9/16/2016 2:36:54', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 202, 2, 210, 1)
    deck.insert_match(dtutil.parse('9/16/2016 10:22:41', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 213, 2, 214, 1)
    deck.insert_match(dtutil.parse('9/16/2016 10:53:13', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 214, 2, 215, 1)
    deck.insert_match(dtutil.parse('9/16/2016 11:09:06', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 213, 2, 197, 1)
    deck.insert_match(dtutil.parse('9/16/2016 11:50:44', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 215, 2, 213, 1)
    deck.insert_match(dtutil.parse('9/16/2016 14:29:28', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 213, 2, 196, 1)
    deck.insert_match(dtutil.parse('9/17/2016 0:06:18', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 216, 2, 202, 0)
    deck.insert_match(dtutil.parse('9/17/2016 0:39:13', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 216, 2, 210, 1)
    deck.insert_match(dtutil.parse('9/18/2016 6:18:19', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 210, 2, 214, 0)
    deck.insert_match(dtutil.parse('9/18/2016 6:45:47', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 213, 2, 210, 1)
    deck.insert_match(dtutil.parse('9/18/2016 9:10:14', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 201, 2, 213, 1)
    deck.insert_match(dtutil.parse('9/18/2016 11:16:10', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 218, 2, 216, 0)
    deck.insert_match(dtutil.parse('9/18/2016 11:43:36', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 214, 2, 216, 0)
    deck.insert_match(dtutil.parse('9/18/2016 12:56:54', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 214, 2, 217, 1)
    deck.insert_match(dtutil.parse('9/19/2016 9:23:26', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 199, 2, 223, 1)
    deck.insert_match(dtutil.parse('9/19/2016 12:31:28', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 218, 2, 203, 1)
    deck.insert_match(dtutil.parse('9/19/2016 13:49:35', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 221, 2, 220, 0)
    deck.insert_match(dtutil.parse('9/19/2016 16:31:42', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 215, 2, 194, 1)
    deck.insert_match(dtutil.parse('9/19/2016 16:57:39', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 206, 2, 194, 1)
    deck.insert_match(dtutil.parse('9/19/2016 17:18:28', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 222, 2, 206, 0)
    deck.insert_match(dtutil.parse('9/19/2016 18:11:13', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 222, 2, 215, 1)
    deck.insert_match(dtutil.parse('9/20/2016 15:50:49', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 190, 2, 220, 0)
    deck.insert_match(dtutil.parse('9/20/2016 20:14:15', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 190, 2, 211, 1)
    deck.insert_match(dtutil.parse('9/21/2016 3:02:24', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 178, 2, 155, 0)
    deck.insert_match(dtutil.parse('9/21/2016 4:22:07', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 221, 2, 206, 0)
    deck.insert_match(dtutil.parse('9/21/2016 18:19:02', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 215, 2, 221, 1)
    deck.insert_match(dtutil.parse('9/21/2016 19:20:31', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 206, 2, 181, 0)
    deck.insert_match(dtutil.parse('9/22/2016 7:39:53', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 223, 2, 221, 1)
    deck.insert_match(dtutil.parse('9/22/2016 12:05:39', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 218, 2, 223, 0)
    deck.insert_match(dtutil.parse('9/22/2016 12:12:55', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 222, 2, 221, 1)
    deck.insert_match(dtutil.parse('9/22/2016 12:59:51', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 222, 2, 223, 0)
    deck.insert_match(dtutil.parse('9/22/2016 13:56:12', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 224, 2, 222, 1)
    deck.insert_match(dtutil.parse('9/23/2016 0:02:20', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 223, 2, 202, 0)
    deck.insert_match(dtutil.parse('9/23/2016 13:33:09', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 155, 2, 226, 1)
    deck.insert_match(dtutil.parse('9/23/2016 14:04:03', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 226, 2, 225, 1)
    deck.insert_match(dtutil.parse('9/24/2016 13:36:55', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 226, 2, 212, 1)
    deck.insert_match(dtutil.parse('9/24/2016 14:14:35', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 218, 2, 212, 1)
    deck.insert_match(dtutil.parse('9/14/2016 18:04:15', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 209, 2, 199, 1)
    deck.insert_match(dtutil.parse('9/18/2016 13:33:32', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 219, 2, 216, 1)
