from typing import Dict, List, Optional
import uuid
from models import College, CollegeCreate, CollegeUpdate

class CollegeStorage:
    def __init__(self):
        self.colleges: Dict[str, College] = {}
        self._initialize_sample_data()

    def _initialize_sample_data(self):
        """Initialize with comprehensive Bangalore colleges data"""
        sample_colleges = [
            # Premier Engineering Institutions in Bangalore
            {
                "name": "Indian Institute of Science",
                "location": "Bangalore, Karnataka, India",
                "type": "public",
                "established": 1909,
                "website": "https://iisc.ac.in",
                "description": "India's premier institute for advanced scientific and technological research and education, ranked #1 in research."
            },
            {
                "name": "IIIT Bangalore",
                "location": "Bangalore, Karnataka, India",
                "type": "public",
                "established": 1999,
                "website": "https://iiitb.ac.in",
                "description": "Public-private partnership institute specializing in Information Technology, Computer Science, and Electronics & Communication."
            },
            {
                "name": "R.V. College of Engineering",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1963,
                "website": "https://rvce.edu.in",
                "description": "One of the top private engineering colleges in Karnataka offering all engineering streams with excellent placements."
            },
            {
                "name": "M.S. Ramaiah Institute of Technology",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1962,
                "website": "https://msrit.edu",
                "description": "Premier private engineering institute known for its academic excellence and industry partnerships."
            },
            {
                "name": "BMS College of Engineering",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1946,
                "website": "https://bmsce.ac.in",
                "description": "One of the oldest engineering colleges in Karnataka with strong alumni network and industry connections."
            },
            {
                "name": "PES University",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1972,
                "website": "https://pes.edu",
                "description": "Leading private university offering engineering, management, medicine, and other professional programs."
            },
            {
                "name": "University Visvesvaraya College of Engineering",
                "location": "Bangalore, Karnataka, India",
                "type": "public",
                "established": 1917,
                "website": "https://uvce.ac.in",
                "description": "Premier government engineering college affiliated to Bangalore University, known for its legacy and excellence."
            },
            {
                "name": "Sir M. Visvesvaraya Institute of Technology",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1986,
                "website": "https://sirmvit.edu",
                "description": "Well-established private engineering college offering undergraduate and postgraduate programs."
            },
            {
                "name": "Dayananda Sagar College of Engineering",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1979,
                "website": "https://dayanandasagar.edu",
                "description": "Popular private engineering college with modern infrastructure and diverse engineering programs."
            },
            {
                "name": "New Horizon College of Engineering",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 2001,
                "website": "https://newhorizonindia.edu",
                "description": "Modern engineering college offering industry-relevant programs with focus on innovation and research."
            },
            {
                "name": "CMR Institute of Technology",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 2000,
                "website": "https://cmrit.ac.in",
                "description": "Growing engineering institute with emphasis on practical learning and industry exposure."
            },
            {
                "name": "Cambridge Institute of Technology",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1999,
                "website": "https://cambridge.edu.in",
                "description": "Private engineering college offering various engineering disciplines with modern facilities."
            },
            # Medical Colleges in Bangalore
            {
                "name": "Bangalore Medical College and Research Institute",
                "location": "Bangalore, Karnataka, India",
                "type": "public",
                "established": 1955,
                "website": "https://bmcri.edu.in",
                "description": "Premier government medical college offering MBBS, MD/MS, and various medical programs."
            },
            {
                "name": "St. John's Medical College",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1963,
                "website": "https://stjohns.in",
                "description": "Prestigious private medical college known for its clinical excellence and research facilities."
            },
            {
                "name": "M.S. Ramaiah Medical College",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1979,
                "website": "https://msrmc.ac.in",
                "description": "Leading private medical college with state-of-the-art facilities and research programs."
            },
            {
                "name": "Kempegowda Institute of Medical Sciences",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1980,
                "website": "https://kims-bangalore.edu.in",
                "description": "Well-established private medical college offering comprehensive medical education."
            },
            {
                "name": "Vydehi Institute of Medical Sciences",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1999,
                "website": "https://vydehi.ac.in",
                "description": "Modern private medical college with advanced medical facilities and research centers."
            },
            # Arts, Science & Commerce Colleges in Bangalore
            {
                "name": "Christ University",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1969,
                "website": "https://christuniversity.in",
                "description": "Prestigious private university offering diverse programs in arts, science, commerce, engineering, and management."
            },
            {
                "name": "St. Joseph's College",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1882,
                "website": "https://sjc.ac.in",
                "description": "Historic college known for excellence in arts, science, and commerce education."
            },
            {
                "name": "Mount Carmel College",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1948,
                "website": "https://mccblr.edu.in",
                "description": "Premier women's college offering undergraduate and postgraduate programs in various disciplines."
            },
            {
                "name": "Jain University",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1990,
                "website": "https://jainuniversity.ac.in",
                "description": "Multi-disciplinary private university offering programs across engineering, management, arts, and sciences."
            },
            {
                "name": "Bangalore University",
                "location": "Bangalore, Karnataka, India",
                "type": "public",
                "established": 1964,
                "website": "https://bangaloreuniversity.ac.in",
                "description": "Major state university offering undergraduate and postgraduate programs across multiple disciplines."
            },
            {
                "name": "St. Joseph's College of Commerce",
                "location": "Bangalore, Karnataka, India",
                "type": "private",
                "established": 1972,
                "website": "https://sjcc.edu.in",
                "description": "Leading commerce college known for its business and management programs."
            }
        ]

        for college_data in sample_colleges:
            college_id = str(uuid.uuid4())
            college = College(id=college_id, **college_data)
            self.colleges[college_id] = college

    async def get_college(self, college_id: str) -> Optional[College]:
        """Get a college by ID"""
        return self.colleges.get(college_id)

    async def get_all_colleges(self) -> List[College]:
        """Get all colleges sorted by name"""
        colleges = list(self.colleges.values())
        return sorted(colleges, key=lambda x: x.name)

    async def create_college(self, college_data: CollegeCreate) -> College:
        """Create a new college"""
        college_id = str(uuid.uuid4())
        college = College(id=college_id, **college_data.dict())
        self.colleges[college_id] = college
        return college

    async def update_college(self, college_id: str, college_data: CollegeUpdate) -> Optional[College]:
        """Update an existing college"""
        if college_id not in self.colleges:
            return None
        
        existing_college = self.colleges[college_id]
        update_data = college_data.dict(exclude_unset=True)
        
        # Update fields that are provided
        for field, value in update_data.items():
            setattr(existing_college, field, value)
        
        return existing_college

    async def delete_college(self, college_id: str) -> bool:
        """Delete a college"""
        if college_id in self.colleges:
            del self.colleges[college_id]
            return True
        return False

    async def search_colleges(self, query: str = "", type_filter: str = "", location_filter: str = "") -> List[College]:
        """Search and filter colleges"""
        colleges = list(self.colleges.values())

        # Apply text search
        if query and query.strip():
            search_query = query.lower()
            colleges = [
                college for college in colleges
                if (search_query in college.name.lower() or
                    search_query in college.location.lower() or
                    (college.description and search_query in college.description.lower()))
            ]

        # Apply type filter
        if type_filter and type_filter != "" and type_filter != "all":
            colleges = [college for college in colleges if college.type == type_filter]

        # Apply location filter
        if location_filter and location_filter != "" and location_filter != "all":
            colleges = [
                college for college in colleges
                if location_filter.lower() in college.location.lower()
            ]

        return sorted(colleges, key=lambda x: x.name)

# Global storage instance
storage = CollegeStorage()

# ...existing code...

storage = CollegeStorage()

# Confirm dataset creation
print(f"Total colleges loaded: {len(storage.colleges)}")
# Optionally, print the names of the first 3 colleges
#for i, college in enumerate(storage.colleges.values()):
    #if i >= 3:
        #break
    #print(f"{i+1}. {college.name}")