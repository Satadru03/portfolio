from dataclasses import dataclass

@dataclass
class Fact:
    heading: str
    emoji: str
    count: int
    data_delay: int

@dataclass
class Skill:
    name: str
    value: int

@dataclass
class Service:
    delay: int
    title: str
    description: str
    icon: str

@dataclass
class Testimonial:
    name: str
    data_delay: int
    work: str
    description: str
    image_location: str
