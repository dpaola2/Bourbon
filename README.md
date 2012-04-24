An example:

	$ curl -X GETATTR http://localhost:5000/
	{'st_ctime': 0, 'st_mtime': 0, 'st_nlink': 2, 'st_gid': 0, 'st_dev': 0, 'st_size': 0, 'st_ino': 0, 'st_uid': 0, 'st_mode': 16877, 'st_atime': 0}
	
	$ curl -X READDIR http://localhost:5000/
	['posts']
	
	$ curl -X GETATTR http://localhost:5000/posts
	{'st_ctime': 0, 'st_mtime': 0, 'st_nlink': 2, 'st_gid': 0, 'st_dev': 0, 'st_size': 0, 'st_ino': 0, 'st_uid': 0, 'st_mode': 16877, 'st_atime': 0}
	
	$ curl -X READDIR http://localhost:5000/posts
	[1]
	
	$ curl -X GETATTR http://localhost:5000/posts/1
	{'st_ctime': 0, 'st_mtime': 0, 'st_nlink': 1, 'st_gid': 0, 'st_dev': 0, 'st_size': 24, 'st_ino': 0, 'st_uid': 0, 'st_mode': 33279, 'st_atime': 0}
	
	$ curl -X READ http://localhost:5000/posts/1
	foobar